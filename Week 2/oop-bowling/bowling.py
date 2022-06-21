class Frame:
    def __init__(self, frame_number, first_try, second_try, third_try = 0):
        self.frame_number = frame_number
        self.first_try = first_try
        self.second_try = second_try
        self.third_try = third_try
        if first_try == 10:
            self.frame = 'strike'
        elif first_try + second_try == 10:
            self.frame = 'spare'
        else:
            self.frame = 'normal' #normal
    
    def __str__(self):
        return f'Frame: {self.frame_number} took down {self.first_try} + {self.second_try} + {self.third_try} pins.'

class Player:
    def __init__(self, name):
        self.name = name
        self.all_frames = [] #will store all the frames

    def add_frame(self, frame):
        self.all_frames.append(frame)

    def calculate_current_score(self):
        score = 0
        if self.all_frames: #not empty
            for i in range(len(self.all_frames)):
                bonus = 0 #reset bonus for each loop
                if self.all_frames[i].frame_number == 10:
                    score += self.all_frames[i].first_try + self.all_frames[i].second_try + self.all_frames[i].third_try + bonus
                else:    
                #normal
                    if self.all_frames[i].frame == 'strike': #bonus is the value of next two balls rolled
                        score+= 10
                        if i+1 < len(self.all_frames): #if there is a next frame
                            if self.all_frames[i+1].frame == 'strike': #bonus is 10 + the next ball
                                bonus += 10
                                if self.all_frames[i+1].frame_number == 10:
                                    bonus += self.all_frames[i+1].second_try #10th frame can bowl again
                                elif i+2 < len(self.all_frames): #second bowl is the next bowl
                                    bonus += self.all_frames[i+2].first_try
                            else: #next frame is normal or spare
                                bonus = self.all_frames[i+1].first_try + self.all_frames[i+1].second_try
                        score += bonus

                    elif self.all_frames[i].frame == 'spare': #bonus is the value of the next ball
                        score += 10
                        if i+1 < len(self.all_frames):
                            bonus = self.all_frames[i+1].first_try
                        score += bonus
                    else:
                        score += self.all_frames[i].first_try + self.all_frames[i].second_try #normal

        return score

class Game:
    def __init__(self, players):
        self.players = players
        self.current_frame = 1
        self.frames_left = 10

    def bowl(self, current_frame, player, first, second, third = None):
        """
        Given a Game instance, a player object, first try score, and second try score,
        update the player's frame.
        """
        if current_frame != self.current_frame: #frame changed
            self.current_frame = current_frame
            self.frames_left = 10 - current_frame

        new_frame = Frame(current_frame, first, second, third) #create a new frame every time a player bowl
        player.add_frame(new_frame)

    def play(self):
        player_score = []
        for player in self.players:
            player_score.append(f'{player.name}: {player.calculate_current_score()}')

        return player_score



##testing
# frame1 = Frame(1,10,0)
# print(frame1)

# anna = Player('anna')
# anna.add_frame(frame1)
# print(anna.calculate_current_score())

# game1 = Game([anna])
# game1.bowl(2, anna, 4,5 )
# print(game1.current_frame)
# print(game1.play())






    



