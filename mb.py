import processing.core as processing

# Define constants
MIN_VAL = -0.5
MAX_VAL = 0.5
MAX_ITERATIONS = 100

def setup():
  """
  Initializes the canvas and sliders.
  """
  processing.size(200, 200)
  processing.pixelDensity(1)

  global min_slider, max_slider, frame_rate_div  # Declare global variables

  min_slider = processing.createSlider(-2.5, 0, -2.5, 0.01)
  max_slider = processing.createSlider(0, 2.5, 2.5, 0.01)

  frame_rate_div = processing.createDiv("")


def draw():
  """
  Calculates and displays the Mandelbrot set.
  """
  load_pixels()

  for x in range(processing.width):
    for y in range(processing.height):
      # Map pixel coordinates to complex plane coordinates
      a = processing.map(x, 0, processing.width, min_slider.value(), max_slider.value())
      b = processing.map(y, 0, processing.height, min_slider.value(), max_slider.value())

      # Initialize complex variables
      ca = a
      cb = b

      n = 0

      while n < MAX_ITERATIONS:
        # Calculate complex number squares
        aa = a * a - b * b
        bb = 2 * a * b

        # Update complex numbers
        a = aa + ca
        b = bb + cb

        # Check for divergence
        if a * a + b * b > 16:
          break

        n += 1

      # Map iteration count to brightness
      bright = processing.map(n, 0, MAX_ITERATIONS, 0, 1)
      bright = processing.map(processing.sqrt(bright), 0, 1, 0, 255)

      # Set pixel color based on iteration count
      if n == MAX_ITERATIONS:
        bright = 0

      index = (x + y * processing.width) * 4
      pixels[index] = bright
      pixels[index + 1] = bright
      pixels[index + 2] = bright
      pixels[index + 3] = 255

  update_pixels()

  # Display frame rate
  frame_rate_div.html(processing.floor(processing.frameRate()))


processing.run(setup, draw)
