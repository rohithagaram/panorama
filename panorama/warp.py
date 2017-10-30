from scipy import ndimage
import homography
import numpy

def panorama(H, fromim, toim, padding=2400, delta=2400, alpha=1):
  import imtools

  is_color = len(fromim.shape) == 3
  if is_color:
    toim_zeros = numpy.zeros((toim.shape[0], padding, 3))
  else:
    toim_zeros = numpy.zeros((toim.shape[0], padding))

  if H[0, 2] < 0:  # fromim is on the right
    toim_t = numpy.hstack((toim, toim_zeros))
  else:
    H_delta = numpy.array([[1, 0, -delta], [0, 1, 0], [0, 0, 1]])
    H = numpy.dot(H, H_delta)
    toim_t = numpy.hstack((toim_zeros, toim))

  fromim_t = imtools.Htransform(fromim, H, (toim_t.shape[0], toim_t.shape[1]))

  if is_color:
    # Three separate checks instead of a * b * c > 0 because of uint8 overflow.
    alpha = ((fromim_t[:, :, 0] > 0) *
             (fromim_t[:, :, 1] > 0) *
             (fromim_t[:, :, 2] > 0)) * alpha
    for col in range(3):
      toim_t[:, :, col] = fromim_t[:, :, col] * alpha + \
                          toim_t[:, :, col]   * (1 - alpha)
  else:
    alpha = (fromim_t > 0) * alpha
    toim_t = fromim_t * alpha + toim_t * (1 - alpha)

  return toim_t
