import av
import cv2
import numpy as np

def start_streaming():
    rtmp_url = 'rtmp://127.0.0.1/live/drone_01'
    
    # 1. ตั้งค่าการดึงภาพจากกล้อง (OpenCV)
    cap = cv2.VideoCapture(0)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = 30

    # 2. เปิด RTMP Container สำหรับการ Write (Muxing)
    # PyAV จะจัดการเรื่อง Protocol และ Format (FLV) ให้เอง
    output_container = av.open(rtmp_url, mode='w', format='flv')

    # 3. สร้าง Video Stream โดยใช้ Encoder H.264
    stream = output_container.add_stream('libx264', rate=fps)
    stream.width = width
    stream.height = height
    stream.pix_fmt = 'yuv420p'
    # ตั้งค่า Bitrate หรือ Option อื่นๆ (เหมือนใน ffmpeg)
    stream.options = {'preset': 'ultrafast', 'tune': 'zerolatency'}

    print(f"Streaming to {rtmp_url} using PyAV")

    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # 4. แปลงภาพจาก BGR (OpenCV) เป็น RGB (PyAV/FFmpeg)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # 5. สร้าง VideoFrame จาก numpy array
            av_frame = av.VideoFrame.from_ndarray(frame_rgb, format='rgb24')
            
            # 6. Encode และส่งข้อมูลออกไป (Mux)
            for packet in stream.encode(av_frame):
                output_container.mux(packet)

            # แสดงภาพตัวอย่าง (Local Preview)
            # cv2.imshow('Drone Mockup (PyAV)', frame)
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break

        # Flush encoder (ส่งข้อมูลที่ค้างอยู่ใน Buffer)
        for packet in stream.encode():
            output_container.mux(packet)

    finally:
        # ปิดทรัพยากร
        output_container.close()
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    start_streaming()
