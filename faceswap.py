import cv2
import insightface
import os
from insightface.app import FaceAnalysis

app = FaceAnalysis(name='buffalo_l')
app.prepare(ctx_id=0, det_size=(640, 640))
swapper = insightface.model_zoo.get_model('inswapper_128.onnx', download=False, download_zip=False)


def faceswap(source_img_path, target_img_path, result_img_path):
    print("faceswap Start!")
    print("source_img_path : ", source_img_path)
    print("target_img_path : ", target_img_path)
    print("result_img_path : ", result_img_path)
    if not os.path.exists(source_img_path):
        return False, "Source image file does not exist"
    if not os.path.exists(target_img_path):
        return False, "Target image file does not exist"
    print("1")
    source_img = cv2.imread(source_img_path)
    # print("source_img : ", source_img)
    if source_img is None:
        return False, "Failed to read the source image"
    print("2")

    target_img = cv2.imread(target_img_path)
    # print("target_img : ", target_img)
    if target_img is None:
        return False, "Failed to read the target image"

    source_faces = app.get(source_img)
    target_faces = app.get(target_img)
    print("3")

    if len(source_faces) == 0 or len(target_faces) == 0:
        return False, "No faces detected"

    source_face = source_faces[0]
    target_face = target_faces[0]

    result = swapper.get(source_img, source_face, target_face)
    cv2.imwrite(result_img_path, result)

    return True, None