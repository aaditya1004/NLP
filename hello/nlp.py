import nltk
import pickle
from nltk.tokenize import word_tokenize
from nltk.classify import NaiveBayesClassifier
import json,os
BASE = os.path.dirname(os.path.realpath(__file__))
# train=[("what is wrong with you","ANGRY"),("what the hell","ANGRY"),("what the hell","ANGRY"),("what the hell","ANGRY"),("Go to hell","ANGRY"),("get lost","ANGRY"),("what the hell","ANGRY"),("hello.","NEUTRAL"),("how are you.","NEUTRAL"),("how are you.","NEUTRAL"),("how are you.","NEUTRAL"),("how are you.","NEUTRAL"),("how are you.","NEUTRAL"),("how are you.","NEUTRAL"),("how are you.","NEUTRAL"),("how are you.","NEUTRAL"),("how are you.","NEUTRAL"),("how are you.","NEUTRAL"),("how are you.","NEUTRAL"),("how are you.","NEUTRAL"),("how are you.","NEUTRAL"),("how are you.","NEUTRAL"),("how are you.","NEUTRAL"),("hi.","NEUTRAL"),("whats up.","NEUTRAL"),("whats up.","NEUTRAL"),("whats up.","NEUTRAL"),("whats up.","NEUTRAL"),("whats up.","NEUTRAL"),("whats up.","NEUTRAL"),("whats up.","NEUTRAL"),("whats up.","NEUTRAL"),("whats up.","NEUTRAL"),("whats up.","NEUTRAL"),("whats up.","NEUTRAL"),("sdhgrhgerhasfqasfasfasf.","NEUTRAL"),("asiudgfusdyhfgv.","NEUTRAL"),("skldhvibviuerv.","NEUTRAL"),("kdghikejrhfvbju.","NEUTRAL"),("bye.","NEUTRAL"),("goodbye.","NEUTRAL"),("good morning.","NEUTRAL"),("good evening.","NEUTRAL"),("good.","NEUTRAL"),("bad.","NEUTRAL"),("good night.","NEUTRAL"),("what is the time.","NEUTRAL"),("hello.","NEUTRAL"),("hi.","NEUTRAL"),("hi.","NEUTRAL"),("hello.","NEUTRAL"),("hello.","NEUTRAL"),("hello.","NEUTRAL"),("hello.","NEUTRAL"),("hello.","NEUTRAL"),("hello.","NEUTRAL"),("hello.","NEUTRAL"),("hello.","NEUTRAL"),("hello.","NEUTRAL"),("hello.","NEUTRAL"),("hello.","NEUTRAL"),("hello.","NEUTRAL"),("hello.","NEUTRAL"),("hi.","NEUTRAL"),("hi.","NEUTRAL"),("hi.","NEUTRAL"),("hi.","NEUTRAL"),("hi.","NEUTRAL"),("hi.","NEUTRAL"),("hi.","NEUTRAL"),("hi.","NEUTRAL"),("hi.","NEUTRAL"),("hi.","NEUTRAL"),("hi.","NEUTRAL"),("And Pierce, confident as ever.","HAPPY"),("Who can forget being awed by the choreographed treadmill dance from Here We Go Again.","HAPPY"),("I can tell you, he is keeping his doctors amused..","HAPPY"),("White was amazed when around 500 people showed up..","HAPPY"),("He has been a wonderful guy from the start and has always accepted my oldest, even though he is not his biological father.","HAPPY"),("Although the storm destroyed many of the buildings along the shore, we feel fortunate that our house did not suffer any damage..","HAPPY"),("We are delighted that you will be coming to visit us. It will be so nice to have you here.","HAPPY"),("He felt invincible and was sure that nobody would beat him.","HAPPY"),("Affectionate children always want to be held in their parents arms and receive lots of hugs and kisses.","HAPPY"),("Wow! I am really impressed that Ashley can speak 7 languages, whereas I only speak one!.","HAPPY"),("In the U.S., Thanksgiving is a holiday in which people give thanks for the blessings they have. Before the Thanksgiving meal, family members will say what they are thankful for.","HAPPY"),("Every morning, Sam is so enthusiastic to begin his day that he jumps out of bed and begins to sing..","HAPPY"),("Iâ€™m Pumped About The Concert This Weekend â€“ Itâ€™s Gonna Be Awesome.","HAPPY"),("I Was Floored By All The Help We Received After Our Son Was In A Serious Accident.","HAPPY"),("i love programming.","HAPPY"),("i am happy that i am going to america.","HAPPY"),("i am esctatic on learning programming.","HAPPY"),("today is my birthday.","HAPPY"),("i like him.","HAPPY"),("yeah.","HAPPY"),("hurrah.","HAPPY"),("i have good friends.","HAPPY"),("I was Content with my situatiopn.","HAPPY"),("I was elated when i heard i was going to USA.","HAPPY"),("Because the waters are halcyon, today is a great day for a boat trip.","HAPPY"),("He went to become a prosperous banker.","HAPPY"),("I was blessed to have him as a friend.","HAPPY"),("The ambience was blissful.","HAPPY"),("The crowd in the stadium were cheerful.","HAPPY"),("i had this euphoric feeling.","HAPPY"),("The felicitous music made me happy..","HAPPY"),("I was fortunate to have him as a friend.","HAPPY"),("I am Glad to have him here.","HAPPY"),("Diwali is a Joyful occation in india.","HAPPY"),("He was Delighted about his new Job.","HAPPY"),("He was esctatic about joining the company.","HAPPY"),("He was elated by the news of his friends arrival.","HAPPY"),("He was Jubilant on hearing the good news.","HAPPY"),("the environment was lively.","HAPPY"),("The ambience was merry.","HAPPY"),("He was Overjoyed by the occasion.","HAPPY"),("The climate in Manali is pleasant.","HAPPY"),("OH!What a pleasant surprise.","HAPPY"),("He was thrilled by the opportunity to meet the president.","HAPPY"),("i am having a good day.","HAPPY"),("She seemed to be the happiest bride I Have ever seen.","HAPPY"),("She was a contented wife..","HAPPY"),("The winner felt elated and excited.","HAPPY"),("It was a joyful occasion..","HAPPY"),("I heard a joyous laughter.","HAPPY"),("They received a euphoric welcome.","HAPPY"),("She had a delighted smile.","HAPPY"),("She gave a gleeful smile.","HAPPY"),("A mirthful laughter.","HAPPY"),("I am happy.","HAPPY"),("I am happy.","HAPPY"),("I am happy.","HAPPY"),("I am happy.","HAPPY"),("I am happy.","HAPPY"),("I am happy.","HAPPY"),("I met a jubilant crowd.","HAPPY"),("The food at the five-star restaurant is awesome.","HAPPY"),("When I graduated from college, I was on cloud nine.","HAPPY"),("The owner of the company is really generous with vacation time.","HAPPY"),("When I sign the lease on my new apartment, I am going to jump for joy.","HAPPY"),("I am honored to accept this position in the company and will work hard to make the team proud.","HAPPY"),("After she said yes to his proposal, he was so happy that he was grinning from ear to ear for weeks after..","HAPPY"),("The cake we had for the holiday was homemade, so it was extraordinarily delicious..","HAPPY"),("Once we lit the fire in the furnace, we all sat down with a cup of chocolate and I was a happy camper.","HAPPY"),("The handmade furniture was perfect for our home and fit just as we expected.","HAPPY"),("I am happy to see you back on your feet only a week after your surgery.","HAPPY"),("Her success in the last three years brought her into the role as a director of the department..","HAPPY"),("All the compliments from my last project were like music to my ears.","HAPPY"),("After her last movie, she became famous in the United States and the U.K..","HAPPY"),("Traveling across the world makes me happy as a clam.","HAPPY"),("I admire people who are generous and kind.","HAPPY"),("The team jaws dropped after finishing a three-year project.","HAPPY"),("Traveling is so exciting that it motivates me to work hard.","HAPPY"),("My brother becomes friends with everyone he meets because his personality is larger than life.","HAPPY"),("It is courageous when people to stand up for what they believe in.","HAPPY"),("got my college acceptance letter this afternoon, it is the best day ever.","HAPPY"),("I am confident that we can find a solution to this problem..","HAPPY"),("I am delighted that I got the job. It is just what I always wanted..","HAPPY"),("When he asked her to marry him she was ecstatic..","HAPPY"),("I am excited by the new opportunities that the internet brings..","HAPPY"),("I feel great today!.","HAPPY"),("Sheâ€™s flying high after the successful product launch.","HAPPY"),("Heâ€™s pumped up for his first half-marathon race this weekend..","HAPPY"),("brilliant.","HAPPY"),("brilliant.","HAPPY"),("brilliant.","HAPPY"),("brilliant.","HAPPY"),("brilliant.","HAPPY"),("brilliant.","HAPPY"),("awesome.","HAPPY"),("awesome.","HAPPY"),("awesome.","HAPPY"),("awesome.","HAPPY"),("awesome.","HAPPY"),("good.","HAPPY"),("good.","HAPPY"),("good.","HAPPY"),("good.","HAPPY"),("good.","HAPPY"),("She was happy to hear the good news..","HAPPY"),("I was overwhelmed by the offer of promotion at work..","HAPPY"),("She was over the moon with her new bicycle and rode it every day for a whole year..","HAPPY"),("She is a very positive person and never lets anything get her down..","HAPPY"),("I feel terrific today!.","HAPPY"),("Going To The World Cup Final Was A Dream Come True.","HAPPY"),("I felt wonderful after such a relaxing weekend..","HAPPY"),("Hours of rehabilitation left him feeling depressed at times.","SAD"),("But she is too bored and depressed to sleep.","SAD"),("I am Sad.","SAD"),("I am Sad.","SAD"),("I am Sad.","SAD"),("I am Sad.","SAD"),("I am Sad.","SAD"),("I am Sad.","SAD"),("I am Sad.","SAD"),("I always feel down in the dumps when I go back to work after a long weekend..","SAD"),("I always feel down in the dumps when I go back to work after a long weekend..","SAD"),("Well, it is ugly, it is awful, but at least it is official..","SAD"),("Then, ashamed and embarrassed, he disappeared under a duvet and grieved.","SAD"),("The more vigilant Allen was, the more resentful and alienated Nicholas became, and the worse things got..","SAD"),("Adopted children must face issues of abandonment as they grow older..","SAD"),("Helen is at the end of her rope after looking for a job for months without any luck..","SAD"),("After his partner died in a car accident, he was left grief-stricken.","SAD"),("The Accidental Prime Minister' director held for GST fraud of at least Rs 34 crore.","SAD"),("Allison broke up with her boyfriend because of his jealous behavior..","SAD"),("Nothing makes me more upset than when I fail my exams. I feel depressed the rest of the day.","SAD"),("Unfortunately, he returned to his friends within minutes feeling rejected after she refused to talk to him..","SAD"),("They were shocked to learn that their beloved neighbor, Miss Ann, had stolen their car. She was such a sweet, 90-year old lady.","SAD"),("After his wife left him, he was so miserable that he stopped shaving, gained 20 kilos, and did not leave the house for weeks at a time..","SAD"),("Her husband is so moody that she never knows if he will be happy or angry when she gets home from work.","SAD"),("Carrie did not feel satisfied with the report she wrote..","SAD"),("The stubborn employee refused to accept that he made a mistake. He kept insisting that he was not wrong.","SAD"),("Ebenezer Scrooge was a stingy old miser who never shared his wealth with anyone..","SAD"),("The actors were humiliated by the newspaper critics review of their new movie..","SAD"),("The respected critic said the film was as pleasant as week-old garbage rotting in the sun.","SAD"),("The cowardly dog refused to leave his hiding spot underneath the bed to help his owner investigate the strange sound outside..","SAD"),("When I found out that Santa Claus was not real, I was so disappointed that all of the presents really came from my parents and not the North Pole.","SAD"),("After Kylie had her heart broken by her ex-boyfriend, she felt so down and blue..","SAD"),("I tried to cheer her up, but she just wants to be sad for awhile.","SAD"),("It is difficult to not become discouraged while looking for a job, especially when you hand out your resume to employers and no one calls you.","SAD"),("Ugh! I don't have anything to do. I'm so bored.","SAD"),("My aunts enjoy inviting me to their romance book club. I always feel trapped because I do not want to hurt their feelings by saying no.","SAD"),("Our friend Lily makes us feel left out when she has a party but does not invite us.","SAD"),("My Heart Sank When I Saw My Test Grade â€“ I Got A 54.","SAD"),("I Was Shaking Like A Leaf After I Heard An Explosion On The Train.","SAD"),("After his grandmother passed away, Ken was so grief-stricken he could not get out of bed.","SAD"),("Even though I am accustomed to traveling for business, I still get homesick if I am away from my home for more than a week..","SAD"),("A year after being fired from his job, Alan is still very bitter. He has a lot of resentment towards his former boss..","SAD"),("His mother became worried when she did not hear from him for two days..","SAD"),("it was such a horrible experience.","SAD"),("it was such a bad day.","SAD"),("bad.","SAD"),("bad.","SAD"),("bad.","SAD"),("bad.","SAD"),("bad.","SAD"),("bad.","SAD"),("bad.","SAD"),("oh what a horrible day.","SAD"),("i dont like programming.","SAD"),("i dont want to go to america.","SAD"),("i am unfortunate to be the criminal.","SAD"),("i am  sad but sad.","SAD"),("i hate cicket.","SAD"),("i do not like cricket.","SAD"),("my friend died today.","SAD"),("i lost my job.","SAD"),("i have bad friends.","SAD"),("I can not bear the tears of a sad child.","SAD"),("She is feeling blue after what has happened to her son.","SAD"),("I am feeling low because my best friend is very ill.","SAD"),("He was depressed by the loss of his son.","SAD"),("Fans were downhearted by the the defeat.","SAD"),("After he failed his English exam, he was depressed for a week..","SAD"),("What is the matter with him? He is so down in the dumps these days..","SAD"),("She was disappointed by her sons poor results at school..","SAD"),("When he heard the news, he became quite emotional..","SAD"),("I felt so embarrassed that I went bright red..","SAD"),("i am not happy.","SAD"),("i am not happy.","SAD"),("i am not happy.","SAD"),("i am not happy.","SAD"),("i am not happy.","SAD"),("i am embarassed.","SAD"),("i am embarassed.","SAD"),("i am embarassed.","SAD"),("i am embarassed.","SAD"),("it was am embarassing situation.","SAD"),("it was am embarassing situation.","SAD"),("As a child she was frightened of the dark..","SAD"),("I'm horrified by the amount of violence on television today..","SAD"),("She was jealous of her sister's new toy..","SAD"),("she hates me.","SAD"),("she hates me.","SAD"),("she hates me.","SAD"),("she hates me.","SAD"),("she hates me.","SAD"),("she hates me.","SAD"),("she hates me.","SAD"),("He is always in a melancholy mood.","SAD"),("He is having a pensive thought about going there.","SAD"),("He is of Wistful nature.","SAD"),("He had a Bittersweet experience.","SAD"),("The condition in India is Deplorable.","SAD"),("He was shocked by this Distressing news.","SAD"),("He has a doleful nature.","SAD"),("He bid farewell Heavyheartedly.","SAD"),("He bid farewell with a  Heavy heart.","SAD"),("He kept on Lamenting.","SAD"),("He was of Melancholic Nature.","SAD"),("Everyone at the funeral were Mournful.","SAD"),("His condition was Pitiful.","SAD"),("He gave a Sorrowful farewell speech.","SAD"),("His demise was tragic.","SAD"),("After 10 years at this company, I just feel jaded..","SAD"),("When you didn't turn up to the meeting, I felt really let down..","SAD"),("I feel very negative about my job - the pay is awful..","SAD"),("It makes me sad to see all those animals in cages at the zoo..","SAD"),("I feel really stressed at work - I need a break..","SAD"),("I've got a blinding headache and I feel terrible..","SAD"),("She's terrified of spiders and screams whenever she sees one..","SAD"),("I was unhappy to hear that I hadn't got the job..","SAD"),("I felt Horrible..","SAD"),("When Dave found out that the plumber charged him double the normal amount to fix his toilet, he felt cheated.","ANGRY"),("I am absolutely furious!! I cannot believe that my dog chewed my favorite shoes. Now they're ruined!.","ANGRY"),("Katie feels threatened every time her boyfriend talks to another girl. She thinks that every girl wants to steal him..","ANGRY"),("I just asked one question to confirm his request, and my boss bit my head off.","ANGRY"),("Sheâ€™s scared to ask for a day off as her boss is in a black mood today..","ANGRY"),("His constant whining drove me up the wall, so I left..","ANGRY"),("Her Chiding drives me crazy.","ANGRY"),("i hate you.","ANGRY"),("angry.","ANGRY"),("i hate you.","ANGRY"),("angry.","ANGRY"),("i hate you.","ANGRY"),("angry.","ANGRY"),("i hate you.","ANGRY"),("angry.","ANGRY"),("i hate you.","ANGRY"),("angry.","ANGRY"),("i hate you.","ANGRY"),("angry.","ANGRY"),("i hate you.","ANGRY"),("angry.","ANGRY"),("i hate you.","ANGRY"),("angry.","ANGRY"),("I was pissed off.","ANGRY"),("I was Livid with him.","ANGRY"),("the incident left me fuming.","ANGRY"),("when she heard about the incident,she suffered a meltdown.","ANGRY"),("I lost my cool when he curse me.","ANGRY"),("i flipped out when he laughed at me.","ANGRY"),("Damn it..","ANGRY"),("The poor girl had not spirit sufficient to upbraid her friend; nor did it suit her now to acerbate an enemy..","ANGRY"),("After he lost the match, he was furious.","ANGRY"),("No one could cool down his infuriation.","ANGRY"),("No one could cool down his infuriating anger.","ANGRY"),("He has problem with my Agreeability.","ANGRY"),("He is always in a state of Miff.","ANGRY"),("No one could handle his Connipation at the meeting.","ANGRY"),("The injustice rankled her.","ANGRY"),("When he did not get his toy, he Raised Hell.","ANGRY"),("After his racist comments, He was Umbraged.","ANGRY"),("My boss is always Ill Tempered.","ANGRY"),("His Ill Humour angered some.","ANGRY"),("His Intervention Excerbated the situation.","ANGRY"),("His Peevishness cannot be handled anymore.","ANGRY"),("His decision enraged many fans.","ANGRY"),("He embittered after the interview.","ANGRY"),("His decision infuriated the fans.","ANGRY"),("His comments Exasparated the audience.","ANGRY"),("The situation at the border Boiled on.","ANGRY"),("We are tired of his tantrums.","ANGRY"),("He Annoys me a lot.","ANGRY"),("He started to agitate during the interview.","ANGRY"),("His comments started to aggravate the matter.","ANGRY"),("His rant was not taken well by a few.","ANGRY"),("The condition here is outrageous.","ANGRY"),("I started an outrage over this issue.","ANGRY"),("He has a nature to provoke his oppositions.","ANGRY"),("he stated his displeasure over this matter.","ANGRY"),("I am Angry.","ANGRY"),("I am Angry.","ANGRY"),("I am Angry.","ANGRY"),("I am Angry.","ANGRY"),("I am Angry.","ANGRY"),("I am Angry.","ANGRY"),("I am Angry.","ANGRY"),("Mom was really upset that we didnâ€™t call to tell we had arrived safely.","ANGRY"),("Iâ€™m Kicking Myself For Not Booking The Flight Yesterday.","ANGRY"),("I get so mad at her when she lies to me.","ANGRY"),("You ate all the cookies. Now Iâ€™m cross with you!.","ANGRY"),("My girlfriend was furious with me when I forgot to pick her up from the airport..","ANGRY"),("The rude comment from his mother-in-law made him livid.","ANGRY"),("i am angry at my friend.","ANGRY"),("i feel like beating my friend.","ANGRY"),("i want to kill him.","ANGRY"),("It Drives Me Up The Wall When People Answer Their Cell Phones In English Class.","ANGRY"),("my friend was killed.","ANGRY"),("i am angry and angry.","ANGRY"),("we lost the match.","ANGRY"),("you did not complete the task.","ANGRY"),("She was angry about the insult..","ANGRY"),("I was cross with her because she didn't invite me to her party.","ANGRY"),("Her comments have always annoyed me.","ANGRY"),("Her tone irritated him.","ANGRY"),("Are you mad at me because I didn't come to your party.","ANGRY"),("My father was furious because I went out without his permission..","ANGRY"),("I'm vexed with you.","ANGRY"),("She was indignant at being the object of suspicion.","ANGRY"),("She received an irate letter from her husband.","ANGRY"),("He was inwardly seething at the offense.","ANGRY"),("She was angry with her boss for criticising her work..","ANGRY"),("I'm very annoyed with him. He hasn't returned any of my calls..","ANGRY"),("They were appalled to hear that they would lose their jobs..","ANGRY"),("I felt a little apprehensive before my interview..","ANGRY"),("How could you say such a thing? You should be ashamed of yourself!.","ANGRY"),("The children have been misbehaving all day - I'm at the end of my tether..","ANGRY"),("He betrayed my trust when he repeated my secret to everyone..","ANGRY"),("I'm sorry I forgot your birthday - I was confused about the dates..","ANGRY"),("Of course I feel cheated - I should have won that competition..","ANGRY"),("I was cross with him for not helping me, as he said he would..","ANGRY"),("I'm very envious of her happiness - I wish I was happy too..","ANGRY"),("I'm very envious of her happiness - I wish I was happy too..","ANGRY"),("I was furious with him for breaking my favourite vase..","ANGRY"),("I get so irritated when he changes TV channels without asking me first..","ANGRY"),("I'm sorry you're upset.","ANGRY"),("I'm sorry you're upset.","ANGRY"),("I'm sorry you're upset.","ANGRY"),("I'm sorry you're upset.","ANGRY"),("I'm sorry you're upset.","ANGRY"),("I didn't mean to be rude..","ANGRY"),("I didn't mean to be rude..","ANGRY"),("I didn't mean to be rude..","ANGRY"),("I didn't mean to be rude..","ANGRY"),("I didn't mean to be rude..","ANGRY"),("My Boss Hit The Ceiling When I Told Him Iâ€™d Lost The Documents..","ANGRY"),("My boss kept criticising me and not the others, so I felt quite victimised..","ANGRY"),("The Movie left me dazed.","CONFUSED"),("I'm a little doubtful about whether to get married or not.","CONFUSED"),("Kelly is so indecisive that she couldn't make a decision if her life depended on it.","CONFUSED"),("Grandpa was very proud of me when I got a promotion at work. He took me out to dinner to celebrate..","CONFUSED"),("He felt uncertain as to whether he should accept the attractive job offer or keep his current, less glamorous job..","CONFUSED"),("He just wasn't sure what to do..","CONFUSED"),("When I see that puzzled look on your face, I know that you didn't understand my question.","CONFUSED"),("i have no idea what to do.","CONFUSED"),("i dont think so.","CONFUSED"),("His ability Amazed me.","CONFUSED"),("He was Astonished by that fact.","CONFUSED"),("He was Baffled by the claim.","CONFUSED"),("He was Bemused by the movie.","CONFUSED"),("He was confounded by claim.","CONFUSED"),("He was Dazed by the experience.","CONFUSED"),("The ride left him disoriented.","CONFUSED"),("Why Would Someone Misinform me.","CONFUSED"),("Thw Clues to the case are Misleading.","CONFUSED"),("The Question Perplexed him.","CONFUSED"),("He was Puzzled by the incident.","CONFUSED"),("He felt an bit unsettled.","CONFUSED"),("He was Lead Astray from his course.","CONFUSED"),("He was Thrown Off Balance.","CONFUSED"),("He was Rattled by the question.","CONFUSED"),("i am confused but confused.","CONFUSED"),("i dont know what happened.","CONFUSED"),("i dont know.","CONFUSED"),("He was bewildered by the choice of computers in the shop.","CONFUSED"),("I was so nonplussed by his announcement that I couldn't say anything..","CONFUSED"),("Are you sure that's what you want?.","CONFUSED"),("I'm reluctant to buy a new car - the one we have is fine..","CONFUSED"),("i am confused.","CONFUSED"),("i am confused.","CONFUSED"),("i am confused.","CONFUSED"),("i am confused.","CONFUSED"),("i am confused.","CONFUSED"),("i am confused.","CONFUSED"),("i am confused.","CONFUSED"),("i am confused.","CONFUSED"),("The farmer's driving directions to the fairground just left us in total confusion.","CONFUSED"),("It was hard to find anything in that confusion in the attic.","CONFUSED"),("thrown into speechless confusion by the wild accusations.","CONFUSED")]
save_train = open(BASE+"//train.pickle", "rb")
train = pickle.load(save_train)
save_train.close()
	  
def trainnew():
	dictionary = set(word.lower() for passage in train for word in word_tokenize(passage[0]))
	t = [({word: (word in word_tokenize(x[0])) for word in dictionary}, x[1]) for x in train]
	classifier = nltk.NaiveBayesClassifier.train(t)
	save_classifier = open(BASE+"//naivebayes.pickle","wb")
	pickle.dump(classifier, save_classifier)
	save_classifier.close()
	return "successful"


def sentiment(input):
	BASE = os.path.dirname(os.path.realpath(__file__))
	data1 =input
	data2 = {word.lower(): (word in word_tokenize(data1.lower())) for word in set(word.lower() for passage in train for word in word_tokenize(passage[0]))}
	classifier_f = open(BASE+"//naivebayes.pickle", "rb")
	classifier = pickle.load(classifier_f)
	x=classifier.classify(data2)  
	print("Your Emotion is:",x)
	classifier_f.close()
	return x



sentiment("i hate you")
# print(train)
# save_train = open("train.pickle","wb")
# pickle.dump(train, save_train)
# save_train.close()