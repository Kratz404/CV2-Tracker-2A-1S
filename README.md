Small little project, adjust the parameters for your own use

Hardware: Arduino board (that pyFirmata support), RC Servo x2 (Any kind)
Library requirements: CV2, face_recognition, pyFirmata

if you get error: AttributeError: module 'inspect' has no attribute 'getargspec'. Did you mean: 'getargs'?
replace with: len_args = len(inspect.getfullargspec(func)[0]
*Solution from: https://stackoverflow.com/questions/74585622/pyfirmata-gives-error-module-inspect-has-no-attribute-getargspec
