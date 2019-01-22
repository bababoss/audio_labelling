
import cv2
class _video_reader(object):
    def __init__(self, video_file):
        self.video_file = video_file

    def __enter__(self):
        cap = cv2.VideoCapture(self.video_file)
        ret, frame = cap.read()  # can you read the source ?
        assert ret == True, "Video read error {}".format(self.video_file)
        cap.set(1, 0)  # set it back to read first frame
        self.cap = cap
        return cap

    def __exit__(self, type, value, traceback):
        ''' TODO: Something intelligent if error occurs '''
        self.cap.release()
        return


class VideoObject(object):

    def __init__(self, video_file):
        self.file_path = video_file

    def get_frames(self, F=None):
        '''
        Get frames of a video one after the other as a list(generator)
        '''
        with _video_reader(self.file_path) as cap:
            ret, frame = cap.read()
            while ret:
                yield F(frame) if F else frame
                ret, frame = cap.read()

    def pull_frames(self, frame_numbers=[], F=None):
        '''
        Get some specific frames of the video as a list(generator)
        '''
        with _video_reader(self.file_path) as cap:
            for frame_number in frame_numbers:
                cap.set(1, frame_number)
                ret, frame = cap.read()
                if ret:
                    yield F(frame) if F else frame

    @property
    def fps(self):
        with _video_reader(self.file_path) as cap:
            fps = cap.get(cv2.CAP_PROP_FPS)
            return fps

    @property
    def width(self):
        with _video_reader(self.file_path) as cap:
            fps = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            return fps

    @property
    def height(self):
        with _video_reader(self.file_path) as cap:
            fps = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            return fps

    @property
    def length(self):
        # total no of frames
        with _video_reader(self.file_path) as cap:
            f_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
            return int(f_count)

    def __len__(self):
        return self.length




if __name__ == "__main__":
    path = "/home/cogknit/PycharmProjects/acc_apigateway/media/scenemedia/output.mkv"
    vid = VideoObject(path)
    lists = vid.get_frames()
    print(type(lists), lists, end=' ')
    count = 0
    for i in lists:
        # print(i,end=' ')
        #cv2.imwrite("frames/{}%d.jpg".format("output") % count, i)
        #         cv2.imshow('image',i)
        #         cv2.waitKey(0)
        #         cv2.destroyAllWindows()
        count += 1
        print(count, end=' ')

