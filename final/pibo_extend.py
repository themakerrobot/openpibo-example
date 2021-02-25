motion_db = {
  "앞":"forward1",
  "앞쪽":"forward1",
  "뒤":"backward1",
  "뒤쪽":"backward1",
  "왼쪽":"left1",
  "오른쪽":"right1",
}

class Pibo_Control:
  def __init__(self):
    self.pd = Pibo_Device(func=self.check_device)
    self.bot_db = {
      "날씨": pe.weather_bot,
      "뉴스": pe.news_bot,
      "사진" : self.pd.picture
    }

    def check_words(self, string="날씨 알려줘", voice=False):
        
        for iti
