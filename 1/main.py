import cv2
import numpy as np

video_cap = cv2.VideoCapture(0)
height = int(video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(video_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter('Result.mp4', fourcc, 30, (width, height))
while True:
    rec, frame = video_cap.read()
    if not rec:
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    width, height = frame_gray.shape

    roi = frame[width // 2 - 100:width // 2 + 100, height // 2 - 100:height // 2 + 100]
    average = np.average(roi)

    if average > 150:
        average = 200
        cv2.putText(frame, 'White', (width // 2 + 5, height // 2 - 5), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2,
                    cv2.LINE_AA)
    elif 80 <= average <= 180:
        cv2.putText(frame, 'Gray', (width // 2 + 5, height // 2 - 5), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2,
                    cv2.LINE_AA)
    else:
        cv2.putText(frame, 'Black', (width // 2 + 5, height // 2 - 5), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0),
                    2, cv2.LINE_AA)

    frame_blur = cv2.blur(frame, (25, 25))

    frame_blur[width // 2 - 100:width // 2 + 100, height // 2 - 100:height // 2 + 100] = roi

    cv2.imshow('output', frame_blur)
    # frame_blur = cv2.cvtColor(frame_blur, cv2.COLOR_GRAY2RGB)
    video_writer.write(frame_blur)

    if cv2.waitKey(1) == ord('q'):
        break
    elif cv2.waitKey(1) == ord('s'):
        cv2.imwrite('Result.jpg', frame_blur)
        break

video_cap.release()
video_writer.release()
