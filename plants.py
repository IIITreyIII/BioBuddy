from abc import ABC, abstractmethod
# Created By: Trey, Nick, Brett
class Plant(ABC):
    def __init__(self, name, description, imagePath, min_temp, max_temp, min_humidity, max_humidity):
        self.name = name
        self.description = description
        self.imagePath = imagePath
        self.min_temp = min_temp  #                  INIT MIN MAX VALUES FOR PLANTS BELOW ##
        self.max_temp = max_temp  
        self.min_humidity = min_humidity  
        self.max_humidity = max_humidity 

    def get_details(self):                                                         ## this function is used to send plant details to main program
        return {'name': self.name, 'description': self.description, 'imagePath': self.imagePath,
         'min_temp': self.min_temp, 'max_temp': self.max_temp,'min_humidity': self.min_humidity, 'max_humidity': self.max_humidity}

class Pansy(Plant):
    def __init__(self):
        description = ("Pansies are a symbol of love and affectionate thoughts .The Pansy is a short-lived perennial and grows to be about 15 to 30 cm tall (6 to 12 inches).Because of its easy upkeep and small size, the pansy is used a common house and garden plant around the world.                                                                                          Pansies typically thrive in a rage of 7C to 18C, (45F to 65F). They can tolerate slightly warmer temperatures but may wilt or suffer heat stress. They prefer a moderate humidity between 40 % - 60 %.                                They can tolerate lower humidity levels but may require more watering.")
        super().__init__("Pansy", description, "pansy.jpg", 7, 18, 35, 60)

   

class PeaceLily(Plant):
    def __init__(self):
        description = ("The Peace Lily is typically grown as a houseplant that originated from Central America and Southeast Asia. While it can grow up to 6 feet tall, it usually only grows to around 3 feet tall in indoor settings. It doesn't have a specific bloom time, so it flowers freely and and is fine to grow in heavy shade.                       They prefer warmer temperatures and thrive between 18C and 27C (65F - 80F), they are sensitive to cold and may experience damage if temps drop below 13C (55F)    Peace Lilys prefer higher humidity levels, ranging between 40% to 60%, lower levels require more watering.")
        super().__init__("Peace Lily", description, "PeaceLily.jpg", 18, 27, 40, 60)



class Fern(Plant):
    def __init__(self):
        description = ("The fern is part of the class Polypodiopsida which is a class of nonflowering, herbaceous vascular plants, some of which go as far back as the Carboniferous Period (beginning about) 358.9 million years ago.  As for size, they range anywhere from small house plants at only 1-1.2 cm (0.39-0.47 in) tall to huge trees ranging from 10 to 25 meters.                                         Ferns prefer a moderate temperatue of 15C to 24C (60F - 75F) and struggle in extreme heat and cold, prefering consistant temperatures.                                            Ferns thrive in high humidity enviorments (50-80%), as they require moist air to support lush foilage, they dehydrate much faster in dry conditions. ")
        super().__init__("Fern", description, "Fern.jpg", 15, 26, 50, 80)


class Pothos(Plant):
    def __init__(self):
        description = ("Pothos is an evergreen plant with thick, waxy, green, heart-shaped leaves with splashes of yellow. Its origins are from Southeastern Asia. It's commonly grown as a hanging plant in households, but also thrives in the wild using the support of trees and its aerial roots. In addition to the overall size, wild Pothos plants can also grow larger leaves in the wild.                                                                          Pothos are adaptable to a wide range of temperatures (15C to 29C) or (60F-85F). They can handle fluctuations in higher temps but not for long periods of time.                                           They are relativley tolerant of humidity with ranges from 40-60%")
        super().__init__("Pothos", description, "Pathos.jpg", 15, 29, 40, 60)
        