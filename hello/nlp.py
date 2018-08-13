import nltk
from nltk.tokenize import word_tokenize
from nltk.classify import NaiveBayesClassifier


train=[("Although the storm destroyed many of the buildings along the shore, we feel fortunate that our house didn't suffer any damage..","happy"),("We are delighted that you will be coming to visit us. It will be so nice to have you here.","happy"),("He felt invincible and was sure that nobody would beat him.","happy"),("Affectionate children always want to be held in their parents' arms and receive lots of hugs and kisses.","happy"),("Wow! I'm really impressed that Ashley can speak 7 languages, whereas I only speak one!.","happy"),("In the U.S., Thanksgiving is a holiday in which people give thanks for the blessings they have. Before the Thanksgiving meal, family members will say what they are thankful for.","happy"),("Every morning, Sam is so enthusiastic to begin his day that he jumps out of bed and begins to sing..","happy"),("i love programming.","happy"),("i am happy that i am going to america.","happy"),("i am esctatic on learning programming.","happy"),("today is my birthday.","happy"),("i like him.","happy"),("yeah.","happy"),("hurrah.","happy"),("i have good friends.","happy"),("i am having a good day.","happy"),("She seemed to be the happiest bride I've ever seen.","happy"),("She was a contented wife..","happy"),("The winner felt elated and excited.","happy"),("It was a joyful occasion..","happy"),("I heard a joyous laughter.","happy"),("They received a euphoric welcome.","happy"),("She had a delighted smile.","happy"),("She gave a gleeful smile.","happy"),("A mirthful laughter.","happy"),("I met a jubilant crowd.","happy"),("The food at the five-star restaurant is awesome.","happy"),("When I graduated from college, I was on cloud nine.","happy"),("The owner of the company is really generous with vacation time.","happy"),("When I sign the lease on my new apartment, Iâ€™m going to jump for joy.","happy"),(" Iâ€™m honored to accept this position in the company and will work hard to make the team proud.","happy"),("After she said yes to his proposal, he was so happy that he was grinning from ear to ear for weeks after..","happy"),("The cake we had for the holiday was homemade, so it was extraordinarily delicious..","happy"),("Once we lit the fire in the furnace, we all sat down with a cup of chocolate and I was a happy camper.","happy"),("The handmade furniture was perfect for our home and fit just as we expected.","happy"),("Iâ€™m happy to see you back on your feet only a week after your surgery.","happy"),("Her success in the last three years brought her into the role as a director of the department..","happy"),("All the compliments from my last project were like music to my ears.","happy"),("After her last movie, she became famous in the United States and the U.K..","happy"),("Traveling across the world makes me happy as a clam.","happy"),("I admire people who are generous and kind.","happy"),("The teamâ€™s jaws dropped after finishing a three-year project.","happy"),("Traveling is so exciting that it motivates me to work hard.","happy"),("My brother becomes friends with everyone he meets because his personality is larger than life.","happy"),(" Itâ€™s courageous when people to stand up for what they believe in.","happy"),(" got my college acceptance letter this afternoon, itâ€™s the best day ever.","happy"),("I'm confident that we can find a solution to this problem..","happy"),("I'm delighted that I got the job. It's just what I always wanted..","happy"),("When he asked her to marry him she was ecstatic..","happy"),("I'm excited by the new opportunities that the internet brings..","happy"),("I feel great today!.","happy"),("She was happy to hear the good news..","happy"),("I was overwhelmed by the offer of promotion at work..","happy"),("She was over the moon with her new bicycle and rode it every day for a whole year..","happy"),("She's a very positive person and never lets anything get her down..","happy"),("I feel terrific today!.","happy"),("I felt wonderful after such a relaxing weekend..","happy"),("Allison broke up with her boyfriend because of his jealous behavior. He never let her talk to other men and always screened her calls..","sad"),("Nothing makes me more upset than when I fail my exams. I feel depressed the rest of the day.","sad"),("Jamie was in a bar with his friends one night when he saw a beautiful girl. He felt confident that night so he went to go talk to her. Unfortunately, he returned to his friends within minutes feeling rejected after she refused to talk to him. Poor Jamie.","sad"),("They were shocked to learn that their beloved neighbor, Miss Ann, had stolen their car. She was such a sweet, 90-year old lady.","sad"),("After his wife left him, he was so miserable that he stopped shaving, gained 20 kilos, and didn't leave the house for weeks at a time..","sad"),("Her husband is so moody that she never knows if he will be happy or angry when she gets home from work.","sad"),("Carrie didn't feel satisfied with the report she wrote. It needed to be perfect to present it to her boss, and it was still missing quite a few details.","sad"),("The stubborn employee refused to accept that he made a mistake. He kept insisting that he wasn't wrong.","sad"),("Ebenezer Scrooge was a stingy old miser who never shared his wealth with anyone..","sad"),("The actors were humiliated by the newspaper critic's review of their new movie. The respected critic said the film was as pleasant as week-old garbage rotting in the sun.","sad"),("The cowardly dog refused to leave his hiding spot underneath the bed to help his owner investigate the strange sound outside..","sad"),("When I found out that Santa Claus wasn't real, I was so disappointed that all of the presents really came from my parents and not the North Pole.","sad"),("After Kylie had her heart broken by her ex-boyfriend, she felt so down and blue. I tried to cheer her up, but she just wants to be sad for awhile.","sad"),("It's difficult to not become discouraged while looking for a job, especially when you hand out your resume to employers and no one calls you.","sad"),("Ugh! I don't have anything to do. I'm so bored.","sad"),("My aunts enjoy inviting me to their romance book club. I always feel trapped because I don't want to hurt their feelings by saying no, but I also don't want to go and listen to sixty-year old women talk about romance.","sad"),("Our friend Lily makes us feel left out when she has a party but doesn't invite us.","sad"),("After his grandmother passed away, Ken was so grief-stricken he couldn't get out of bed.","sad"),("Even though I am accustomed to traveling for business, I still get homesick if I am away from my home for more than a week..","sad"),("A year after being fired from his job, Alan is still very bitter. He has a lot of resentment towards his former boss..","sad"),("His mother became worried when she didn't hear from him for two days..","sad"),("it was such a horrible experience.","sad"),("it was such a bad day.","sad"),("oh what a horrible day.","sad"),("i dont like programming.","sad"),("i dont want to go to america.","sad"),("i am unfortunate to be the criminal.","sad"),("i am  sad but sad.","sad"),("i hate cicket.","sad"),("i do not like cricket.","sad"),("my friend died today.","sad"),("i lost my job.","sad"),("i have bad friends.","sad"),("I can't bear the tears of a sad child.","sad"),("She's feeling blue after what has happened to her son.","sad"),("I am feeling low because my best friend is very ill.","sad"),("He was depressed by the loss of his son.","sad"),("Fans were downhearted by the the defeat.","sad"),("After he failed his English exam, he was depressed for a week..","sad"),("What's the matter with him? He's so down in the dumps these days..","sad"),("She was disappointed by her son's poor results at school..","sad"),("When he heard the news, he became quite emotional..","sad"),("I felt so embarrassed that I went bright red..","sad"),("As a child she was frightened of the dark..","sad"),("I'm horrified by the amount of violence on television today..","sad"),("She was jealous of her sister's new toy..","sad"),("After 10 years at this company, I just feel jaded..","sad"),("When you didn't turn up to the meeting, I felt really let down..","sad"),("I feel very negative about my job - the pay is awful..","sad"),("It makes me sad to see all those animals in cages at the zoo..","sad"),("I feel really stressed at work - I need a break..","sad"),("I've got a blinding headache and I feel terrible..","sad"),("She's terrified of spiders and screams whenever she sees one..","sad"),("I was unhappy to hear that I hadn't got the job..","sad"),("When Dave found out that the plumber charged him double the normal amount to fix his toilet, he felt cheated.","angry"),("I am absolutely furious!! I cannot believe that my dog chewed my favorite shoes. Now they're ruined!.","angry"),("Katie feels threatened every time her boyfriend talks to another girl. She thinks that every girl wants to steal him..","angry"),("i am angry at my friend.","angry"),("i feel like beating my friend.","angry"),("i want to kill him.","angry"),("my friend was killed.","angry"),("i am angry and angry.","angry"),("we lost the match.","angry"),("you did not complete the task.","angry"),("She was angry about the insult..","angry"),("I was cross with her because she didn't invite me to her party.","angry"),("Her comments have always annoyed me.","angry"),("Her tone irritated him.","angry"),("Are you mad at me because I didn't come to your party.","angry"),("My father was furious because I went out without his permission..","angry"),("I'm vexed with you.","angry"),("She was indignant at being the object of suspicion.","angry"),("She received an irate letter from her husband.","angry"),("He was inwardly seething at the offense.","angry"),("She was angry with her boss for criticising her work..","angry"),("I'm very annoyed with him. He hasn't returned any of my calls..","angry"),("They were appalled to hear that they would lose their jobs..","angry"),("I felt a little apprehensive before my interview..","angry"),("How could you say such a thing? You should be ashamed of yourself!.","angry"),("The children have been misbehaving all day - I'm at the end of my tether..","angry"),("He betrayed my trust when he repeated my secret to everyone..","angry"),("I'm sorry I forgot your birthday - I was confused about the dates..","angry"),("Of course I feel cheated - I should have won that competition..","angry"),("I was cross with him for not helping me, as he said he would..","angry"),("I'm very envious of her happiness - I wish I was happy too..","angry"),("I'm very envious of her happiness - I wish I was happy too..","angry"),("I was furious with him for breaking my favourite vase..","angry"),("I get so irritated when he changes TV channels without asking me first..","angry"),("I'm sorry you're upset - I didn't mean to be rude..","angry"),("My boss kept criticising me and not the others, so I felt quite victimised..","angry"),("I'm a little doubtful about whether to get married or not.","confused"),("Kelly is so indecisive that she couldn't make a decision if her life depended on it.","confused"),("Grandpa was very proud of me when I got a promotion at work. He took me out to dinner to celebrate..","confused"),("Craig felt uncertain as to whether he should accept the attractive job offer or keep his current, less glamorous job. He just wasn't sure what to do..","confused"),("When I see that puzzled look on your face, I know that you didn't understand my question.","confused"),("i have no idea what to do.","confused"),("i dont think so.","confused"),("i am confused but confused.","confused"),("i dont know what happened.","confused"),("i dont know.","confused"),("He was bewildered by the choice of computers in the shop.","confused"),("I was so nonplussed by his announcement that I couldn't say anything..","confused"),("Are you sure that's what you want?.","confused"),("I'm reluctant to buy a new car - the one we have is fine..","confused"),("i am confused.","confused"),("The farmer's driving directions to the fairground just left us in total confusion.","confused"),("It was hard to find anything in that confusion in the attic.","confused"),("thrown into speechless confusion by the wild accusations.","confused")]# train=[("i am not happy","sad"),("i am not happy","sad"),("i am not happy","sad"),("i am not happy","sad"),("i am not happy","sad"),("angry","angry"),("angry","angry"),("angry","angry"),("angry","angry"),("angry","angry"),("sad","sad"),("sad","sad"),("sad","sad"),("sad","sad"),("sad","sad"),("sad","sad"),("sad","sad"),("sad","sad"),("happy","happy"),("happy","happy"),("happy","happy"),("happy","happy"),("happy","happy"),("happy","happy"),("happy","happy"),("happy","happy"),("happy","happy"),("happy","happy"),("happy","happy"),("i am cofused","confused"),("i am cofused","confused"),("i am cofused","confused"),("i am cofused","confused"),("i am cofused","confused"),("i am cofused","confused"),("i am cofused","confused"),("i am cofused","confused"),("i am very happy","happy"),("i am very happy","happy"),("i am very happy","happy"),("i am very happy","happy"),("i am very happy","happy"),("i am very happy","happy"),("i am very sad","sad"),("i am very sad","sad"),("i am very sad","sad"),("i am very sad","sad"),("i am very sad","sad"),("i am very sad","sad"),("i am very sad","sad"),("i am very sad","sad"),("i am very angry","angry"),("i am very angry","angry"),("i am very angry","angry"),("i am very angry","angry"),("i am very angry","angry"),("i am very angry","angry"),("i am very angry","angry")]


def sentiment(nlp):
	dictionary=set(word.lower() for passage in train for word in word_tokenize(passage[0]))
	t = [({word: (word in word_tokenize(x[0])) for word in dictionary}, x[1]) for x in train]
	classifier = nltk.NaiveBayesClassifier.train(t); xr={};data1 =nlp;data2 = {word.lower(): (word in word_tokenize(data1.lower())) for word in dictionary};  xr=classifier.classify(data2); print(xr); return xr

    

sentiment("hi")


# def sentiment(input):
# 	return input