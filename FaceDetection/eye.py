import cv2,numpy, os, argparse


DEFAULT_OUTPUT_PATH = 'EyeCaptureImages/'
DEFAULT_CASCADE_INPUT_PATH = '/usr/local/share/OpenCV/haarcascades/haarcascade_eye.xml'

# Define class to capture video
class VideoCapture:

	def __init__(self):
		self.count = 0
		self.argsObj = Parse()
		self.eyeCascade = cv2.CascadeClassifier(self.argsObj.input_path)
		
		# assign VideoCapture of cv2 to videoSource - 0 is first video of webcam object in computer
		self.videoSource = cv2.VideoCapture(0)

	def CaptureFrames(self):
		while True:
			# Create a unique number for each frame
			frameNumber = '%08d' % (self.count)

			# Capture frame by frame
			ret, frame = self.videoSource.read()

			# Set screen color to gray, so the haar cascade can easily detect the edges an eyes
			screenColor = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

			# Cusomize how cascade detects your eye
			eyes = self.eyeCascade.detectMultiScale(
				screenColor,
				flags=cv2.CASCADE_SCALE_IMAGE)

			# Display the resulting frame
			cv2.imshow('Spying on you', screenColor)

			# If length of eyes equal to zero, there have been no eyes detected
			if len(eyes) == 0:
				pass

			# If a eye is detected, eyes return 1 or more depending on the amount of eyes detected 
			if len(eyes) > 0:
				print('Eyes detected')

				# Graph the eye and draw the rectangle around it
				for (x,y,w,h) in eyes:
					cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 255), 2)

				cv2.imwrite(DEFAULT_OUTPUT_PATH + frameNumber + '.png', frame)

			# Increement count so we get a unique name for each frame
			self.count += 1

			# If press 'ESC' close the video
			if cv2.waitKey(1) == 27:
				break

		# When everything is done, release the capture and close window
		self.videoSource.release()
		cv2.waitKey(500)
		cv2.destroyAllWindows()
		cv2.waitKey(500)


def Parse():
	parser = argparse.ArgumentParser(description='Cascade path for eye detection')
	parser.add_argument('-i', '--input_path', type=str, default=DEFAULT_CASCADE_INPUT_PATH, help='Cascade input path')
	parser.add_argument('-o', '--output_path', type=str, default=DEFAULT_OUTPUT_PATH, help='Output path for pictures taken')
	args = parser.parse_args()
	return args



def ClearImageFolder():
	if not(os.path.exists(DEFAULT_OUTPUT_PATH)):
		os.makedirs(DEFAULT_OUTPUT_PATH)

	else:
		for files in os.listdir(DEFAULT_OUTPUT_PATH):
			filePath = os.path.join(DEFAULT_OUTPUT_PATH, files)
			if os.path.isfile(filePath):
				os.unlink(filePath)
			else:
				continue

def main():
	ClearImageFolder()

	#Instantiate class object
	eyeDetectImplmentation = VideoCapture()

	# Call CaptureFrames class to begin eye detection
	eyeDetectImplmentation.CaptureFrames()

if __name__ == '__main__':
	main()












