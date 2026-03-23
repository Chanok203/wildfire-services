-- 1. เคลียร์ทางให้ Schema Edge (สำหรับข้อมูลจากหน้างาน/โดรน)
INSERT INTO "edge"."hotspots_p30" (geom) VALUES (ST_SetSRID(ST_MakePoint(0, 0), 4326));
INSERT INTO "edge"."hotspots_p45" (geom) VALUES (ST_SetSRID(ST_MakePoint(0, 0), 4326));
INSERT INTO "edge"."hotspots_p60" (geom) VALUES (ST_SetSRID(ST_MakePoint(0, 0), 4326));

-- 2. เคลียร์ทางให้ Schema Warroom (สำหรับข้อมูลสรุป/วิเคราะห์บน VPS)
INSERT INTO "warroom"."hotspots_p30" (geom) VALUES (ST_SetSRID(ST_MakePoint(0, 0), 4326));
INSERT INTO "warroom"."hotspots_p45" (geom) VALUES (ST_SetSRID(ST_MakePoint(0, 0), 4326));
INSERT INTO "warroom"."hotspots_p60" (geom) VALUES (ST_SetSRID(ST_MakePoint(0, 0), 4326));