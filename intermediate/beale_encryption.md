# Title

Encoding with the Beale Cipher

# Difficulty

Intermediate

# Tags

encryption, cipher

# Description

You may recall the story of [Thomas J. Beale](https://en.wikipedia.org/wiki/Beale_ciphers), who (legend has it) worked with his cohorts to mine treasure over two years, then secretly bring it back to Virginia and hid it. He described the location of the treasure in a document encoded using the US Declaration of Independence as a key. Each number in the ciphertext corresponded to a word from the Declaration of Independence from which you take the first letter. 

Today's challenge is to *encode* a message using this Beale cipher. There will be multiple solutions to any phrase, but your message should be able to decrypt your message using the solution from your Beale decoder. 

Remember, Beale's ciphers discard anything not in the A-Z alphabet, so you'll have to drop whitespace and punctuation. Yes it makes decryption a bit harder. 

## Declaration of Independence

When in the course of human events it becomes necessary for one people to dissolve the political bands which have connected them with another and to assume among the powers of the earth the separate and equal station to which the laws of nature and of nature's god entitle them a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation we hold these truths to be self evident that all men are created equal that they are endowed by their creator with certain unalienable rights that among these are life liberty and the pursuit of happiness that to secure these rights governments are instituted among men deriving their just powers from the consent of the governed that whenever any form of government becomes destructive of these ends it is the right of the people to alter or to abolish it and to institute new government laying its foundation on such principles and organizing its powers in such form as to them shall seem most likely to effect their safety and happiness prudence indeed will dictate that governments long established should not be changed for light and transient causes and accordingly all experience hath shown that mankind are more disposed to suffer while evils are sufferable than to right themselves by abolishing the forms to which they are accustomed but when a long train of abuses and usurpations pursuing invariably the same object evinces a design to reduce them under absolute despotism it is their right it is their duty to throw off such government and to provide new guards for their future security such has been the patient sufferance of these colonies and such is now the necessity which constrains them to alter their former systems of government the history of the present king of great Britain is a history of repeated injuries and usurpations all having in direct object the establishment of an absolute tyranny over these states to prove this let facts be submitted to a candid world he has refused his assent to laws the most wholesome and necessary for the public good he has forbidden his governors to pass laws of immediate and pressing importance unless suspended in their operation till his assent should be obtained and when so suspended he has utterly neglected to attend to them he has refused to pass other laws for the accommodation of large districts of people unless those people would relinquish the right of representation in the legislature a right inestimable to them and formidable to tyrants only he has called together legislative bodies at places unusual uncomfortable and distant from the depository of their public records for the sole purpose of fatiguing them into compliance with his measures he has dissolved representative houses repeatedly for opposing with manly firmness his invasions on the rights of the people he has refused for a long time after such dissolutions to cause others to be elected whereby the legislative powers incapable of annihilation have returned to the people at large for their exercise the state remaining in the meantime exposed to all the dangers of invasion from without and convulsions within he has endeavored to prevent the population of these states for that purpose obstructing the laws for naturalization of foreigners refusing to pass others to encourage their migration hither and raising the conditions of new appropriations of lands he has obstructed the administration of justice by refusing his assent to laws for establishing judiciary powers he has made judges dependent on his will alone for the tenure of their offices and the amount and payment of their salaries he has erected a multitude of new offices and sent hither swarms of officers to harass our people and eat out their substance he has kept among us in times of peace standing armies without the consent of our legislatures he has affected to render the military independent of and superior to the civil power he has combined with others to subject us to a jurisdiction foreign to our constitution and unacknowledged by our laws giving his assent to their acts of pretended legislation for quartering large bodies of armed troops among us for protecting them by a mock trial from punishment for any murders which they should commit on the inhabitants of these states for cutting off our trade with all parts of the world for imposing taxes on us without our consent for depriving us in many cases of the benefits of trial by jury for transporting us beyond seas to be tried for pretended offenses for abolishing the free system of English laws in a neighboring province establishing therein an arbitrary government and enlarging its boundaries so as to render it at once an example and fit instrument for introducing the same absolute rule into these colonies for taking away our charters abolishing our most valuable laws and altering fundamentally the forms of our governments for suspending our own legislature and declaring themselves invested with power to legislate for us in all cases whatsoever he has abdicated government here by declaring us out of his protection and waging war against us he has plundered our seas ravaged our coasts burnt our towns and destroyed the lives of our people he is at this time transporting large armies of foreign mercenaries to complete the works of death desolation and tyranny already begun with circumstances of cruelty and perfidy scarcely paralleled in the most barbarous ages and totally unworthy the head of a civilized nation he has constrained our fellow citizens taken captive on the high seas to bear arms against their country to become the executioners of their friends and brethren or to fall themselves by their hands he has excited domestic insurrections amongst us and has endeavored to bring on the inhabitants of our frontiers the merciless Indian savages whose known rule of warfare is an undistinguished destruction of all ages sexes and conditions in every stage of these oppressions we have petitioned for redress in the most humble terms our repeated petitions have been answered only by repeated injury a prince whole character is thus marked by every act which may define a tyrant is unfit to be the ruler of a free people nor have we been wanting in attention to our British brethren we have warned them from time to time of attempts by their legislature to extend an unwarrantable jurisdiction over us we have reminded them of the circumstances of our emigration and settlement here we have appealed to their native justice and magnanimity and we have conjured them by the ties of our common kindred to disavow these usurpations which would inevitably interrupt our connections and correspondence they too have been deaf to the voice of justice and of consanguinity we must therefore acquiesce in the necessity which denounces our separation and hold them as we hold the rest of mankind enemies in war in peace friends we therefore the representatives of the united states of America in general congress assembled appealing to the supreme judge of the world for the rectitude of our intentions do in the name and by authority of the good people of these colonies solemnly publish and declare that these united colonies are and of right ought to be free and independent states that they are absolved from all allegiance to the British crown and that all political connection between them and the state of great Britain is and ought to be totally dissolved and that as free and independent states they have full power to levy war conclude peace contract alliances establish commerce and to do all other acts and things which independent states may of right do and for the support of this declaration with a firm reliance on the protection of divine providence we mutually pledge to each other our lives our fortunes and our sacred honor .

#  Input Description

You'll be given a sentence, one per line, that serve as your plaintext. Example:

    Hello, world!

# Output Description

Your program should emit a string of numbers that encode the plaintext in Beale's cipher. Example:

1268, 777, 881, 1319, 496, 718, 610, 987, 337, 138

That's one valid output for it. Another might be:

1052, 950, 652, 652, 1150, 415, 369, 1159, 423, 1117

And so on.

# Challenge Input

    I have deposited in the county of Bedford, about four miles from Buford's, 
    in an excavation or vault, six feet below the surface of the ground, the 
    following articles

# Challenge Output

641, 623, 823, 1135, 499, 527, 950, 1018, 402, 38, 3, 794, 777, 527, 1011, 552, 1297, 484, 1278, 68, 528, 640, 781, 214, 238, 198, 1201, 587, 1196, 475, 1187, 115, 1259, 878, 280, 1284, 374, 765, 679, 1284, 845, 1084, 562, 370, 489, 777, 1093, 1009, 1159, 770, 751, 580, 412, 1009, 109, 872, 249, 720, 724, 1199, 1097, 1051, 965, 495, 1048, 821, 1322, 237, 641, 496, 392, 128, 1293, 821, 1231, 845, 236, 842, 455, 118, 1049, 587, 777, 921, 700, 1278, 351, 266, 985, 1188, 1325, 193, 518, 319, 795, 404, 943, 649, 1034, 858, 1263, 459, 962, 777, 688, 399, 528, 1078, 928, 901, 538, 1052, 1001, 1167, 1047, 778, 1074, 109, 1273, 520, 272, 116, 903, 316, 1004, 460, 533, 489, 1034, 38

# Python Solution

    def beale_cipher(plaintext, decl):
        def _startswith(ch, ideclrange):
            for i in ideclrange:
                if i[1].lower().startswith(ch.lower()):
                    return i[0]
        idecl = map(lambda x: x[0], zip(enumerate(decl.split(), 1)))
        res = []
        for ch in plaintext.replace(" ", ""):
            i = random.randint(1, len(idecl))
            app = _startswith(ch, idecl[i:])
            if app:
                res.append(app)
            else:
                # maybe we went too far, start from beginning
                res.append(_startswith(ch, idecl))
        return res
