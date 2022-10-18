class Logo:
    def __init__(self, brand="", description="", score=0, image_src=""):
        self._brand = brand
        self._description = description
        self._score = score
        self._image_src = image_src

        #getters
        def get_brand(self):
            return self._brand
