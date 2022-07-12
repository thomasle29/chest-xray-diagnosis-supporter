from Infrastructure import util

class App:
    '''
    App class
    Manufacturing application function of this service
    '''
    def __init__(self) -> None:
        self.util = util.Util()

    def chestDiagnosis(self, image):
        machine = self.util
        result = machine.compute_gradcam(image)

        return result