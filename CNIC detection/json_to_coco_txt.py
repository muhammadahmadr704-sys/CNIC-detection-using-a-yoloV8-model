import glob
import cv2
from pathlib import Path
import json
import os

if __name__ == '__main__':

    out_dir = "D:\\TruiD\\haris_images\\new_data_haris_phone\\val\\"
    # os.makedirs(out_dir, exist_ok=True)

    for filename in glob.glob("D:\\TruiD\\haris_images\\new_data_haris_phone\\val/*.json"):

        out_yolo = [0]
        h, w, c = cv2.imread(filename.replace("json", "jpg")).shape

        with open(filename, "r") as f:
            tt = f.read()
            ann_json = json.loads(tt)["shapes"]
            for shape in ann_json:
                if shape["label"] == "document":
                    points = shape["points"]
                    points = [points[0][0] / w, points[0][1] / h, points[1][0] / w, points[1][1] / h]
                    points_yolo_rect = [(points[0] + points[2]) / 2, (points[1] + points[3]) / 2, points[2] - points[0],
                                        points[3] - points[1]]
                    out_yolo.extend(points_yolo_rect)
                if shape["label"] == "visible" or shape["label"] == "hidden":
                    points_yolo_kpt = [shape["points"][0][0] / w, shape["points"][0][1] / h,
                                       float(2.0) if shape["label"] == "visible" else float(1.0)]
                    out_yolo.extend(points_yolo_kpt)

        with open(os.path.join(out_dir, Path(filename).stem + ".txt"), "w") as f:
            yolo_txt = " ".join(map(str, out_yolo))
            f.write(yolo_txt)