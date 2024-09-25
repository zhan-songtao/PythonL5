import cv2
import dlib


# 读取图片
img = cv2.imread('images/01.png')
# 转换成灰度图像
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 在下方书写你的代码
# 生成人脸检测器
detector = dlib.get_frontal_face_detector()
# 检测人脸
faces = detector(gray_img,1)
# 显示文字的字体
font = cv2.FONT_HERSHEY_SIMPLEX
# 检测到人脸
if len(faces) != 0:
    # 将检测到的人脸数量写到图像中
    # print('faces:' + str(len(faces)))
    cv2.putText(img, 'faces:' + str(len(faces)), (10, 30), font, 1, (0, 0, 255), 2)
# 没有检测到人脸
else:
    # 添加文字 no face
    # print('no face')
    cv2.putText(img, 'no face', (10, 30), font, 1, (255, 255, 255), 1)

# 显示图像
cv2.imshow("image", img)
# 设置图像显示时长
cv2.waitKey(0)
# 关闭窗口
cv2.destroyAllWindows()
