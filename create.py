# create_dataset.py
import os, json
from textwrap import dedent

def write_jsonl(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

train_samples = [
    # --- INDIA (4) ---
    {
        "country": "India",
        "theme": "dharma vs desire",
        "deities": ["Shiva", "Parvati"],
        "prompt": "Write a 600–900 word original mythological short story set in Varanasi on the banks of the Ganga. Tone: lyrical but clear. Show a conflict between duty (dharma) and personal longing. Include gentle sensory detail (bells, river light, incense) and end with a reflective moral that avoids preaching.",
        "response": dedent("""\
            The bell of dawn trembled across Varanasi and shook a silver ladder down the Ganga. In that light walked Meera, daughter of a boatman, palms perfumed with sandal from the morning puja. Her father reminded her, as he always did, that the river was a witness to vows; one must take care what is promised near water. Meera promised only to row cleanly, to bind the boat true, to accept the marriage chosen for her—a quiet sari of a life.

            Yet desire has the stealth of a cat in ghats. A young sculptor from the lane of images had begun to bring her father lamp oil. He carved Shiva and Parvati from neem, his hands steady as breath on a conch. He told Meera that the city itself was a mandala: circles of duty, circles of love, turning to the same center. She listened and then folded the words like a note under her tongue, to melt or remain.

            On the night before her betrothal, a long wind lifted the river. The sculptor’s newest murti—Ardhanarishvara, half Shiva, half Parvati—fell with a soft cry from his bench and cracked. He ran to the ghats where Meera’s boat floated, roped as tightly as her future. “Help me take it to the water,” he said. “Let Ganga decide whether the image lives.”

            “My father forbids work at night,” Meera whispered. “And my promise forbids more.” Still, the image in two halves lay like divided moonlight. The sculptor’s eyes were rivers where two seasons argued. Meera untied the rope.

            They lowered the broken form into the shallows, and the Ganga took it on her palm. A small whirl rose, soft as a yawn. From the whirl, a votive flame drifted toward them, although no hand had released it. The flame paused between the two halves of the image and rested, unafraid, in the crack.

            Somewhere a bull snorted; somewhere anklets rang over stone. Meera felt the world lean. She reached into the water, pressed the halves together, and the crack gentled until it was no more than a line like a life-line on a palm. The image grew warm, as if breath moved through it. A fragrant wind carried the scent of wild jasmine not in season.

            A presence stood with them—felt before seen. Shiva’s stillness, Parvati’s kindness: not two, not one, a meeting the city had always known. No terror, only recognition, as if duty and longing were two banks holding the same water.

            “Child,” said a voice as soft as bell-metal, “dharma is not the chain you fear, nor desire a fire that must burn all boats. When Parvati loved, she loved with the patience of mountains; when Shiva kept his vow, he kept it with the vastness of sky. Balance is the oar.”

            The flame winked out; the night returned to its ordinary courage. In the morning, Meera went to her father. She told him that she would not run from the marriage; neither would she smother the part of her that leaned toward carving and learning. She asked that the sculptor be allowed to teach her to work in wood so that she could help mend the images brought cracked to the ghat.

            Her father’s silence was a deep well. Then he laughed once, short, and shook his head. “The river teaches differently to every swimmer,” he said. “Row cleanly.”

            Years later Meera’s house smelled of camphor and lemon oil. She mended images and listened to pilgrims. She learned that desire, when put to service, steadies the hand; that duty, when warmed by love, stops sounding like iron. On some evenings she and her husband set lamps upon little leaf-boats and pushed them into the river. Each lamp went where it would, yet all drifted toward the same darker gold.

            The moral was never carved on any door: Promises should not drown the heart, and the heart should not break its promises. Between the two, a quiet ferry crosses, if the oar knows both water and shore.""")
    },
    {
        "country": "India",
        "theme": "the descent of the river",
        "deities": ["Bhagiratha", "Ganga", "Shiva"],
        "prompt": "Compose an original legend echoing, but not copying, the Ganga’s descent. Set it in a small Himalayan village watching for a life-giving stream. Keep the tone humble and respectful; end with a single-line proverb of your own invention.",
        "response": dedent("""\
            The village had a thirst that lived in the wood of doorframes and the cracks of grain jars. Snow shone on high ridges, too far for a child’s legs, too near for a drought’s patience. Old Ama, who mended shawls, said that once a stream had run through here, singing a tune learned from glaciers. “It lost its way,” she told the children, like a grandmother rescuing a story from silence.

            Tashi, who tended goats, went up the slope with a bowl of barley and three marigolds. His grandmother had taught him that offerings were invitations, not bribes. Where the slope turned to scrim of cloud, he placed the bowl and listened. He heard nothing first, and then something like a thread being pulled through cloth.

            Ganga, who is river and mother and mirror, came not as a roar but as a bright thinking. “Child,” the thought said, “water can come heavy and break what it loves, or it can come gentle and stay.” Tashi bowed in his small way. “Come as the village can hold,” he answered.

            Below, the elders lit lamps. On the third night, a pilgrim with ash in his hair and starlight in his eyes walked into the village. He wore a crescent moon without weight and leaned on a trident that seemed to carry more journeys than iron could. He looked at the dry channel and then at the ridgeline. “A stream asks for a bearer,” he said. “My matted locks have held the wildness of a great river before. For your stream, a single strand is enough.”

            He plucked a hair and planted it in the dust as if it were seed. When dawn loosened the sky, the strand had become a root of water that trembled, then ran, then laughed. The channel remembered its work. Children ran beside it with copper cups. Goats kneeled, unbidden, as if to pray.

            The pilgrim was gone before anyone could ask his name, but the village said thank you to every god they had learned and to the ones they hadn’t. Ama dipped her finger in the new stream and marked each child’s brow with a cool crescent. Tashi took the empty barley bowl and set it on the water. It spun once, then again, and then steadied as if learning itself.

            The stream never grew grand. It grew faithful. Fields of buckwheat learned a new shade of green. Potters returned to their wheels. The thirst in doorframes loosed its grip.

            The proverb the children learned: “May our blessings fit our hands, and still fill our jars.”""")
    },
    {
        "country": "India",
        "theme": "wisdom disguised",
        "deities": ["Saraswati"],
        "prompt": "Write a story where learning comes disguised as a mistake. Set it in a rural school by a banyan tree. Include a short two-line poem within the story. Keep it gentle and reflective.",
        "response": dedent("""\
            Under the banyan that held a thousand small classrooms in its shade, the village school kept its slate boards stacked like dusk. Lata, quick with sums but impatient with silence, painted a goddess’s veena across her slate when she should have been practicing letters. The paint bled into the grooves; her teacher sighed.

            “If the river runs on the road,” he said, “the fields go hungry.” He wiped the slate clean and left a white ghost of strings. Lata burned with shame. She stopped drawing for forty days, and the banyan learned her silence.

            On exam day a wind rose, pulling the chalk dust into a thin storm. The roof tin rattled like coins in a careless hand. The questions blurred. Lata’s letters, practiced hard, would not sit straight. She closed her eyes and heard, somewhere under the noise, the memory of strings. She drew a line—one, two, three—until the lines gathered like a veena. On the lines she wrote her answers, each word resting on a note.

            When the storm passed, the teacher saw what she had done. He frowned, then laughed without sound, as if a well had surprised him by being deeper than he thought. “Who told you to make music for your words?”

            “No one,” Lata said, “and also—someone.” The banyan leaves shook; a white egret stepped near and dipped its head. In the margin of Lata’s paper appeared a couplet she did not remember writing:

            “Where letters fear to walk alone,  
            A song will lead them safely home.”

            That evening, the teacher placed a small veena pendant on the classroom shrine. “Saraswati teaches in the spaces we call errors,” he told the children. Lata drew again after that, not on slates meant for sums, but on paper where the lines waited like strings. Mistake became doorway, and doorway became lesson. The banyan learned her laughter again, and the river kept to the field without losing its song.""")
    },
    {
        "country": "India",
        "theme": "hospitality and humility",
        "deities": ["Krishna"],
        "prompt": "Retell an original village-scale legend where a mysterious cowherd tests hospitality. Avoid direct reuse of well-known episodes; keep it fresh. End with a soft moral in one sentence.",
        "response": dedent("""\
            In a drought, the village of Amla measured kindness by ladles. A stranger came at dusk with dust on his flute and cows that looked like moons fallen to earth. He asked for water for the herd first, himself last. Some houses shut their doors to save their pitchers. Old Basanti opened hers.

            She poured water into a trough until the clay sang cool. The cows drank as if remembering a river from another life. The stranger drank last, then mended Basanti’s broken fence with a rope that seemed more blessing than fiber. At midnight a wind rose sweet as mango blossom out of season. In the morning, the trough ran by itself, a thread of water the village could not empty however many ladles they dipped.

            Only then did Basanti notice the peacock feather left on her windowsill. She touched it to her brow and understood nothing and everything at once—the kind of understanding that makes more humble, not more proud.

            Moral: When you pour last for yourself, the pitcher learns how to fill itself.""")
    },

    # --- NEPAL (4) ---
    {
        "country": "Nepal",
        "theme": "origin of the valley",
        "deities": ["Manjushri"],
        "prompt": "Compose a legend about draining a great lake to found a city in the valley. Keep it distinct from canonical versions: focus on a young mason who listens to advice in dreams. Use respectful Buddhist imagery and a serene tone.",
        "response": dedent("""\
            Before the city, a lake slept in the lap of hills. Boats were prayers with oars. A young mason named Pasang dreamed each night of a lotus whose stem was a stair. In the dream a gentle voice—neither male nor female, both mountain and bell—told him to build a door for the water.

            He told elders; they shook their heads. Lakes do not use doors. But the dream persisted, adding details like a patient teacher: a notch in the ridge, a line of chiseled stone, a shrine for gratitude beside the cut. Pasang gathered five friends and began to work at dawn when the mist made the world kind.

            When their chisels struck right, the sound was a syllable that made birds change direction. A traveler came by, staff tipped with light. His gaze was clear, like someone who had read a book and become the book. He watched without interrupting. When Pasang’s strength faltered, the traveler lifted a single rock that should have taken four men and set it where it wanted to be.

            At last the notch became a doorway. The lake pressed its forehead to the threshold and bowed. Water walked out, slow and shining, into terraces that were not yet fields and streets that were not yet streets. On the far hill, the traveler raised his hand. A lotus shone where future roofs would glitter.

            Pasang built the gratitude shrine and placed a single book there, blank pages waiting. The traveler—Manjushri, some said later—wrote the first word on the first page: “Listen.” The valley kept listening. Cities grew that remembered doorways. Rivers learned to leave without quarrel. And in spring the terraces looked like someone had written poems all in green, every line in meter.""")
    },
    {
        "country": "Nepal",
        "theme": "compassion and courage",
        "deities": ["Avalokiteshvara"],
        "prompt": "Write a gentle mountain tale where a child climbs to rescue a prayer flag in a storm and learns what true courage is. Include one short mantra-like line in transliteration (invented, not canonical).",
        "response": dedent("""\
            The prayer flags above Thulo Gaun had frayed into bright birds. When a storm pulled one loose, it snagged on a ledge no adult could reach without ropes. Pema, small and stubborn, went at dawn with a sling and a pocket of roasted corn. “Courage is not shouting,” her grandmother had said. “It is breathing well.”

            The path grew narrow until it was a question. Clouds pulled wool over the ridge. Pema’s breath counted itself: in-two-three, out-two-three. At the ledge she saw the flag tangled around a thornbush clinging like a last thought. She spoke to the mountain the way she spoke to goats—kindly, as if it could misunderstand.

            A presence gathered, like many hands agreeing. In the rustle of the bushes she heard a kindness too large for one throat. “Little one,” it seemed to say, “fear is a bell; let it ring and pass.” Pema loosened the knot with fingers that trembled and obeyed. She tucked the flag inside her jacket and began the careful descent, repeating a line that came to her on its own: “Oṃ mani jayate hridaya.”

            When she reached the village, the storm gave up its anger. They tied the flag again, high and laughing. Pema’s grandmother kissed her brow. “You learned the courage that keeps others warm,” she said. Above them, the prayer flags spoke all languages at once and meant the same: may all find a safe path down.”""")
    },
    {
        "country": "Nepal",
        "theme": "craft and patience",
        "deities": ["Vajrapani"],
        "prompt": "Tell a story about a bell maker in Patan who rushes an order for a festival and must start over. Include a teaching about strength guided by patience.",
        "response": dedent("""\
            In Patan, where metal remembers every hand, Dorje the bell maker agreed to cast a great bell in seven days. Festival drums hurried his blood. He poured too hot; the mold cracked like pride. The bell rang once—a broken sound like a promise kept badly.

            Shamed, Dorje closed his shop. In the quiet night a traveler stopped, shoulders broad as a doorway, eyes kind as oil lamps. He examined the failed bell, then sat with Dorje among the molds like a teacher among restless boys.

            “Strength without patience bends metal the wrong way,” the traveler said. “Patience without strength never pours.” Dorje listened as if to rain on a roof. They rebuilt the mold with slower hands. They let the alloy rest as if it too had a right to breathe. When they poured again, the metal flowed like a thought corrected.

            At the festival, the bell rang a note that started in the ground and rose to the moon. Dorje did not boast. He placed his hand on the bronze and felt a smaller bell ringing inside his ribs—the one that had learned to wait and then act. People asked for the traveler’s name. Dorje smiled. “A friend who knows how thunder learns to walk.” Some said Vajrapani had come as a craftsman. Dorje only tightened his apron and taught his apprentices to count to thirty between breaths.""")
    },
    {
        "country": "Nepal",
        "theme": "Kumari and ordinary kindness",
        "deities": ["Kumari (living goddess)"],
        "prompt": "Create an original tale about a day when the Kumari witnesses an act of anonymous kindness in the city and learns something about divine and ordinary care. Keep it respectful and gentle.",
        "response": dedent("""\
            From her window, the Kumari watched a city move like many bracelets. People waved without names. One afternoon a cart lost a wheel near the square. The crowd gathered, full of advice and thin on hands. A sweeper from the far lane set down her broom and lifted the cart alone until the axle could be wedged. No one noticed except the child goddess, who noticed everything.

            That night, candles were lit; drums spoke. The Kumari received bows and mustard oil lamps, all the forms. But she kept seeing the sweeper’s back, the plain courage of it. In a dream she walked outside without paint or crown and found the sweeper mending a sandal with thread pulled from her own shawl.

            “I am supposed to bless you,” the Kumari said, and felt silly, as children do when they hear themselves from the outside.

            “Then let us bless each other,” the sweeper said, and broke her bread in two. They ate. In the morning, the Kumari woke certain that divinity travels both directions like a road. When she gave darshan that day, she also sent a small wrapped parcel to the sweeper: a pair of sandals, sturdy and plain. No one recorded it. The city, which keeps its best books unwritten, remembered anyway.""")
    },

    # --- PAKISTAN (4) ---
    {
        "country": "Pakistan",
        "theme": "love & fate",
        "deities": ["Folk heroes (Sassi, Punnu)"],
        "prompt": "Retell an original, modern-voiced folktale inspired by Sassi–Punnu without copying plots. Set it by the Hingol River. Include desert imagery and a bittersweet ending with dignity.",
        "response": dedent("""\
            Along the Hingol, thornbush writes its alphabet on wind. Sassi sold clay pots painted with fish that had learned to fly on her walls. A traveler came riding a motorbike that coughed like an old camel and laughed like a boy. He bought two pots and left a woven wristband that smelled faintly of petrol and cardamom.

            Seasons exchanged bracelets. They met again when the river ran low and stones told truths. The traveler taught Sassi how to mend engines with patience; she taught him how to keep water cool in the throat of clay. People talked. They always do when love uses tools instead of drums.

            One night a sandstorm lifted like a curtain. The traveler’s family arrived with the old questions about honor and the newer ones about debt. He looked at Sassi as a man looks at a road that is both home and horizon. “I cannot ask you to leave your river,” he said. “I cannot pretend I do not want to.”

            She gave him a pot painted with a fish that refused to be sensible. “Carry water,” she said, “even if it is only memory.” He left before dawn. Sassi heard the motorbike fade like a prayer that chooses to be small rather than loud. Years later her shop still smelled of clay and rain that hadn’t fallen yet. When the river ran, she filled a pot and poured it into sand where the wristband had once lain. The desert kept the secret and, perhaps, the blessing: love that does not possess still waters the road.”""")
    },
    {
        "country": "Pakistan",
        "theme": "river guardians",
        "deities": ["Indus spirits"],
        "prompt": "Write a river-guardian tale set near Sukkur. A child learns to respect the Indus by releasing a fish back. Include a single-sentence moral at the end.",
        "response": dedent("""\
            The bridge at Sukkur threw its red ribs over the Indus like a careful giant. Bilal caught a small fish in a plastic cup and ran to show his grandfather. The old man’s hands smelled of nets and cumin. “A river is not a cupboard,” he said gently.

            They walked to the bank where the reeds wrote soft things. Bilal tipped the fish back. It paused, surprised by freedom, then flickered into the green. A curl of current rose, shaped almost like a hand blessing through water. Bilal felt watched in a way that made him kinder rather than afraid.

            That night he dreamed of a woman with riverweed in her hair placing small lamps along the edge of sleep. “Guard what guards you,” she said, and her voice sounded like many streams speaking together. In the morning, Bilal carried a bag and gathered trash along the bank. The river seemed to breathe easier.

            Moral: When you return what is not yours, the river returns you to yourself.""")
    },
    {
        "country": "Pakistan",
        "theme": "truth and song",
        "deities": ["Shah Abdul Latif Bhittai (as inspiration)"],
        "prompt": "Create a story in which a traveling singer in Sindh helps a village resolve a dispute about a well. Keep it respectful to Sufi traditions; end with a couplet in simple English.",
        "response": dedent("""\
            Two families claimed one well in Kachch. The water turned bitter with their quarrel. A singer came with a tanpura wrapped in burlap and a smile wrapped in silence. He sat between them and tuned a note until goats stopped chewing and listened.

            “If truth is a mirror,” he sang, “it breaks when you hold it like a stone.” He told a parable of two sisters who shared one pot: the pot did not break because they filled it with turns. The families argued less loudly. The singer asked each to draw water in alternating hours for forty days while he stayed to sing at dusk.

            The song became a habit, then a bridge. People began to hear the well’s rope creak as if it had a voice. On the last evening the singer poured his own cup back into the well and sang a couplet he left like a lamp:

            “The heart is a shared well—draw gently, take turns;  
            What each returns as water, the other returns as burns.”""")
    },
    {
        "country": "Pakistan",
        "theme": "mountain hospitality",
        "deities": ["Fairy Meadows spirits"],
        "prompt": "Tell an original tale set near Fairy Meadows where a lost trekker is sheltered by unseen helpers. Keep the tone respectful and leave the spirits unnamed.",
        "response": dedent("""\
            Clouds braided themselves around Nanga Parbat and forgot how to unbraid. A trekker lost the trail and his courage at the same time. Night came down wearing wolves’ feet. He found a hut whose door stood open like a sentence waiting for a verb. Inside, a fire burned with no smoke, tea steamed with no owner.

            He drank, cried a little, slept like a child returned to himself. In the morning, the door had a garland of tiny alpine flowers someone had placed while he dreamed. Outside, fresh prints led to the right path, not quite human, not quite deer. He left a tin of biscuits and a thank-you written on a map edge:

            “For the ones who make strangers into guests.” The mountain did not answer, which was its way of saying yes.""")
    },

    # --- SRI LANKA (4) ---
    {
        "country": "Sri Lanka",
        "theme": "guardians of the sea",
        "deities": ["Kataragama"],
        "prompt": "Compose an original coastal myth in southern Sri Lanka where fishermen invoke Kataragama before a storm. Include sea-sensory detail and end with a proverb-like line.",
        "response": dedent("""\
            The sea smelled of lime and iron the day the sky tied a knot. Fishermen in Kirinda set little flags on their masts and whispered names learned from grandfathers. A boy, Arjun, carried a tray with fruit and a small spear of wood to the edge where waves practiced arriving.

            Wind rose. Nets threshed on shore like restless horses. A pilgrim in red and saffron stood near the shrine, bare feet reading the sand. He touched the wooden spear and it felt suddenly heavier, as if it remembered forests. “Courage is not refusing to fear,” he said, “but making a place for it to sit without steering.”

            The boats went out singing. The storm came in teaching. At the height of the lesson, a band of calmer water opened like an eye. Through it the fleet slipped, nets lifted by hands that were not on board. When they returned, the pilgrim was gone, the spear planted near the shrine, seawater beading on it as dew beads on leaves at dawn.

            The old men nodded as if a story had come home from a long errand. The catch fed the village, and the line they told their children was simple: “Honor what you ask help from, and help what you honor.”""")
    },
    {
        "country": "Sri Lanka",
        "theme": "forest and forgiveness",
        "deities": ["Veddah forest spirits"],
        "prompt": "Write a tale set near Dambana where a hunter must atone for felling a sacred tree. Keep it respectful to indigenous traditions; the spirits should guide rather than punish.",
        "response": dedent("""\
            In Dambana, Kalan cut a tree that had once sheltered wedding songs. He did not know its story; hunger can make ears small. That night he dreamed of antlers made of branches and eyes made of rain. The spirit asked nothing first; it listened.

            In the morning, Kalan stood where the stump told its age in circles. He brought honey and apology. Elders joined him, and together they planted three saplings, not one. For a season he carried water to them as a man carries his child the first mile. The spirit returned in a dream only to show him a grove in the future where his grandchildren would shade their rice.

            Kalan learned to ask the forest before taking, and to leave twice what he took in care. Forgiveness, he found, was not a word but a work that trees understand perfectly.""")
    },
    {
        "country": "Sri Lanka",
        "theme": "island of stories",
        "deities": ["Local sea spirits"],
        "prompt": "Create a fable about a storyteller who trades his voice to the sea for a tale and must earn it back by teaching children to listen. End with one line of gentle moral.",
        "response": dedent("""\
            The storyteller of Matara grew proud and loud. One night he shouted at the sea, “Give me a tale no one has heard.” The sea agreed, on a price: his voice until he could make others’ voices brighter than his own.

            He wrote stories on sand; the waves read them and clapped. He taught children to collect shells not for necklaces but for listening—each shell a different whisper. They began to tell their own stories, small and exact. The sea, satisfied, placed his voice back on his tongue like a shell returned to shore.

            Moral: Keep the door of the ear wider than the door of the mouth.""")
    },
    {
        "country": "Sri Lanka",
        "theme": "hospitality of hills",
        "deities": ["Sri Pada (Adam’s Peak) guardians"],
        "prompt": "Tell an original pilgrimage tale up Sri Pada where strangers share tea, and a sign reminds them that holiness often arrives as hospitality.",
        "response": dedent("""\
            The steps up Sri Pada counted pilgrims better than pilgrims counted steps. Lila’s sandals broke at dawn; a woman she had never met handed her a pair of rope sandals that fit as if kind. A tea seller poured tea sweeter than his prices. A monk tied a string around her wrist and said nothing at all.

            Near the summit the clouds cleared like curtains taken back by shy hands. On the rock, sunlight made a shape that people argued about and loved anyway. Lila realized that the mountain had been holy long before the view. She left her rope sandals at a small shrine on the way down with a note pinned to them: “For the feet behind me.” The note flapped like a small prayer flag.

            On such trails, the sign is not thunder but tea shared without question.""")
    },
]

valid_samples = [
    # 2 per country
    {
        "country":"India",
        "theme":"festival and compassion",
        "deities":["Hanuman"],
        "prompt":"Write a 500–800 word tale set during Diwali in a small town where a mischievous child learns compassion through a meeting with a humble stranger linked to Hanuman. Keep it respectful, warm, and original.",
        "response":"During Diwali, the lanes of Kashi Nagar crackled with lamps and impatience. Raju had saved fireworks and unkindness in equal measure... (story continues with a meeting with a quiet traveler who helps an injured dog; the child learns service is the brightest lamp)."
    },
    {
        "country":"India",
        "theme":"rain after drought",
        "deities":["Indra"],
        "prompt":"Compose an original village story about calling the rains without blame or fear. Avoid clichés; end with a one-line proverb.",
        "response":"The drum-maker’s courtyard was a map of cracks. When prayers for rain turned sour with blame, an old woman suggested a festival of thanks before the rains. Children painted clouds on empty pots... (ending proverb: 'Gratitude plants the sky before it opens.')."
    },

    {
        "country":"Nepal",
        "theme":"bridge of kindness",
        "deities":["Tara"],
        "prompt":"Write a serene valley story where villagers build a small bridge together after a flood, guided by a green-robed traveler. Use gentle Buddhist imagery.",
        "response":"After the flood, two hamlets faced each other like estranged cousins. A traveler in a green shawl showed them how to lash bamboo and patience... (the bridge becomes a habit of visiting, not just crossing)."
    },
    {
        "country":"Nepal",
        "theme":"snow and silence",
        "deities":["Chenrezig"],
        "prompt":"Create a tale in which a shepherd learns to hear compassion in silence during winter. Keep it meditative.",
        "response":"Snow simplified the hills until even goats walked like monks. The shepherd, Sonam, lost a lamb in white weather... (he carries the lamb back and learns that silence can be a voice)."
    },

    {
        "country":"Pakistan",
        "theme":"desert well",
        "deities":["Local desert spirits"],
        "prompt":"Tell a respectful folktale where a caravan saves a hidden desert well by covering it after use, taught by unseen guardians.",
        "response":"The caravan found a well the color of dates. Greed wanted to widen it, but a wind wrote no in sand... (they learn to cover and leave a jug; later travelers survive because care traveled first)."
    },
    {
        "country":"Pakistan",
        "theme":"city kindness",
        "deities":["Sufi saint (unnamed)"],
        "prompt":"Write a Karachi night story where a rickshaw driver helps a lost student, and both feel blessed by a quiet presence near a shrine.",
        "response":"Neon and dust made Karachi a galaxy on the ground. A rickshaw driver took a student far for little fare... (near the shrine, the air grows soft; they part lighter)."
    },

    {
        "country":"Sri Lanka",
        "theme":"tea and rain",
        "deities":["Hill spirits"],
        "prompt":"Compose a hill-country tale in a tea estate where pickers share water during a heatwave and call the rain with songs taught by elders.",
        "response":"The leaves turned crisp under a white sun. Elders taught a song that was more breathing than tune... (rain arrives gently; the estate manager learns to count in cups, not kilos)."
    },
    {
        "country":"Sri Lanka",
        "theme":"lagoon lights",
        "deities":["Nagha guardians"],
        "prompt":"Create a lagoon-side myth where children release lamps on leaf boats and learn about caring for water creatures watched by gentle snake-guardians. Avoid fear; keep it tender.",
        "response":"At the lagoon, the children’s leaf boats carried lamps and small promises. A coil of water moved like a necklace... (they rescue a tangled turtle; the guardians approve with ripples)."
    },
]

if __name__ == "__main__":
    write_jsonl("data/train.jsonl", train_samples)
    write_jsonl("data/valid.jsonl", valid_samples)
    print("Wrote:", "data/train.jsonl", f"({len(train_samples)} lines)", "and", "data/valid.jsonl", f"({len(valid_samples)} lines)")
