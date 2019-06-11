from scipy.signal import find_peaks
from peakutils.peak import indexes
# a="FBHJLZINOHBYTYCNCZLUYZUFIGDMZMYKVQDSPUEFJIGJPOQUFQDRJQJNTVDREXXJEOQGDUUWFWGOXQQHKJLUWFDYCMFRZTUIKVHHZPATEHKKLHUTWRLTZTQZIGEOCEIFISWNPPDQPAHSMFHXFTWNPEYSFTDSTMOYISHZSBJXLFYOGFTYYSRXOFQQRBGZSFEUVBQONIUXCSIZMFXNERJGGFJMVADTOPKWVOURJNQRDOOGYDUXKCUYEIUNIHLSPJDYYSHIZMELZQDRDQEYCWJNECKYNVDZTGSFCOPOEZXFUBWHPGQQCSQZSFTNECVGFSIBFIOJEIUDJHLRWIQAVURTPPKYECWCTUXFSOQMMVJFNVLSAFHRRMEKYPJFTQRXOJDLKCDTPXIYLRBZSBJXRMVJTOEXRIUYDUYQCVDJAMUSKMRLGJCFERYORPHQVOGOYHKUKCWNPNQXJSAZTOSYZCQGEUXJVBGUQUXJTFHZLDUTLGSKCJEIISYKLMUILGLTRIKLVGLSFMQYZCQYEIQYRFHTPXJTGOOKZOJTCCJEEIUKZBGOYHCFIYVZSFBFKSVZEVHSZBDJPCQYVCYKCXXJKVHXOJDTJOXXDXUWVOOXPBTDZBWKCNYSRZGKNMYSVPBZSFJNDSGUZNIIRMVZCVSPZBDJOJJNFBWNPTJZUMVIFUJNEUHJRFQUGFRGNISTLZGNPMFZJPHZEFHQFCNHLDAFKDDYEFDAZFRTXFDYRZWACNENCOQJWFQWEWQLTOUWUSWGTMMMRHZKXJWMKSAVPDJKICPSZEUWEQOOXBJJTVDTRFVTIAHGYEVTIOOUEPVUVCSRPUXFKKLYSUXNJHKKEFQRYOVKYEUIWCUSPBTJTWVOZOCFUSLZDFURVRDYTGXJYOGHPFDUCOBOYHMNKVXYLMBMZGOOQFYKVSOYZSHDWCUZSPIJNVRCLOJYFQRSAFJJWCUSPTINJHKXZOUNKGLSAPIXZPOKEIYXBWGODVDNHIHSPTINZGDTLMYJEHKGEEUIZQDZPTXNDGHRQUEUCOBOYHMNKVKAXBDXZVDBPGKSCWNKLDXNCRLTEIUXKFHKEXXJEHKKOBOHFAHYHIUSZAQUEFDOFMLTRJJNNWORWFQAVTRUECQQCAHYDJYXKVHHPTJUCOBKCJDYYSZUCMTGPGRSPEYXKOQIPIUXCWNKLQBFPGWGEJESYSFGYUQPVOGBLOJFXSRLPWUWPALYEBAJNSPGVFJMRHLYXFQSUAHYDJMJISUORIJZGHKKCFQGJCOAEFBDCSWSPFCGIOFKEIUJJCXXLELJIGLZJGEWNWVKXFDXRMLZTTJMVKLYPTJHFIUYPJWSFFDTNFYXKVHIFSIJFTJUOLDTNZHJRFYXKVHCTOWBYSUKHJJMNSIRJUEMVOYKYUXNJZLLPXXNTVKGOCUJEHKKEPCGFTKODWYWKIHGYEEKYWVNZOEZIWVHFUQBRZNOYHIMRRRCLQETIDOGJFHYYOWYESKYJOQJQSUYJVLYSPKWLDRTEIUXKOJKLOTYYSQODIUFIRQUXPHJZHLYLUQQVHRROCOFEWGOZUVZCZRLDPKSUOQJQVHDJWJTTGONEUQUEIYSXOIZPSJMVPLMMBDLZHZGDDEQUOQJMMQHBOQJEIUSKVHXPXQXCWJNEOEBWCUZSFVNIGWZTNUFJHUUYPCJIGKGGFWQZASYPEJMRHGGHOEKKVHAYJLJIGHZSJHYVSQHTMBNFBBKLSIFXCZNPOJMVSDXWJUXKGWGCTMJISWACOYSXCQZSFBNXVWOYUXJTCVSTDTFIYQKDTQSUWIZSBJNJBRZPOEZXVWNPZCFPVDBPEUYVQWKONOXKSUOZVIIRFNSLUJJIOWCZSAYFCWNPHBNDDVKNPDXZGWKOPVFWOLTESQIZCVOROQQWFRSOFUUJDDIPQYHBSGAACOFEOQZPODFKVDZTTIQZUKZWZRNXUHXEIQSRFHLCJWJIOWUCBDITCVZDMUXJHKGYGYAVALRWJESSIWOYDUWKOLTHBOXTOQMZCQHBAXISGQWKVHXTOJNDSDTOEYXKOQIPUXFEHKKNFBJSFDZPECZCHLHTMBNFBGUWMQWYIEHWFIURQHZPMUXTCSKUVTISCZSLOEKRFLFZOQXKOWKFOYAVFVOEZBJRRDAEIEWFTDYEVTDZBMUFSDFCBDZFSUXRWGZSFINXBDRNBCJWFRSEIUAVFBLTSIYFPMKNUINEHKKFOYAVFVKLTYYNOVKXFHLZBJUFUEKUOUQYFIXKKRNFOTWVRPOWMYTEMHGCTQKKSUZSFRNXPDTRTUJZBJZSFKSZJHXDFZZJHOORIJNEUXVPWUSKVRARIYYNOVUYMOFWOLTETYLEOOODFLJEARXPJCUFFWGYUJMRBWNPCYLSOQMMFSFLGHCPBHJDOGKZGIYRFVZFGVFERVUHFQWVUOOXQINEUDZZVHTIWJOYTQNUOVZCPDTDSUXTDXFIRHRWJIBYCZGDOEYZBYUWWUIZBWNPQHTASFZEIUXZUQGWTXTNSGAYFNUVQWKOMOHFZGZPNFJIOWACFIFERDTFOKXLOORJQHTECXTNFTBRJHCSFDFJHUUYPCJIGWXTFTYFTLMFSUTLHZNJUXJSSVZPYFQRBDZTPDBRGWNLUUQLGLBPEQWBADZEFHRRMKGGFRJVBDZHPHPZTYKCJVNVRWNLUMTLZGHPUXJWWUYEDESWWUSLUYTECIOETANERRLOBHPDOWZPSMMZQKODBIZSGWGYUYFCDDXEPVYYSXTTWUWJSWNLUIHZSQZTTJXYOYKMFUSJSDXNIYSXTRXZWUWUSFGOFINWQRTQJHRVRWNTTTNJQRBPSOIVGHXGFIYNCQUMFBUIWCKDGEWSCWNNBFYLFLTRUXJJWJTLMEKKVHLTSIYJHDXDBDIGCWKYUYFCRDXVNQYKSUIZOVNIADZTPDXRWGNLSLFIRDYESESFAHXLWYQFSECSPMFJBRZABHYFTWNPSUXVOUISUUFDQDAEJESZBJZSBJJOHUGZSTNEOUENMQNDGUKBVYWVSAZCBEWUWQGCZUAZRHTNFXJJOLJTOTJGSQJPOJYVGWYLSUSVSGKOUEAVFLLJUXJWWQJTOWXSCZSLOQLISHJTOTJGSQJPOJYVGWYLSUSVSGKOFLJEHKUFHXMZGWKLNIUVBWZHPOJRFVJZVRQVOQJESYUCSFNPDANEUWNPJHBFFNOEJIFKWPKZGJMVIQOGFHXVKHXPBBQPRRTZUASFKDTJUXNEUDHZVJGFKPGYTQNUVHYLJTYYSGODDEAVFBODMYPVHKKQJHXKGHTEFDHVWQGYFQWCMFNLQJJICIZSFXNJHRXJPVYYSFUDNEXKVLYTTDTKVLTRUXFKOVZCPDTDSUYNPKQUOFZFBBQPGHKTOVFTHLZTTQQCWQJTSUHKPDYPEESTVDTRFINEHKKHBLJCSQMEIIUICGANFTGPFDJTPINXBDRDUXJVOURJVDNMSUYPXQXUOUQLOTHFZGLTMBJUKLZSKKXKVBJCPWJEOQJSFBNLARTNFIYRFVLZSCJUHKKJFCNKHHJFMJWRJLUWFJQZUKZTOJTKVHJLSAFISDYMFJBVSQZSFCYYOWAWUHFMWRRPUBNXVWISBDLVGWNPFDJIUBYTHDFKIUKZGXDUFRMPOQYFAVHZXCFEGDOOBIYICQUXFHXCCRQPEQYRGSKNJVNTKDBPMUSXHKOQUXJISZKCFIYRFVGYEKQKFDBTPBJKZLMSUJMVMZUFMTXVSRTPTYLEOWACFYKKVHXPXUWVBRYEBHXKVHEHPKQUGHKLOEYYSUZSFOXRKDIWFQWSIWLLJDYJWJTLMIMFKLTRUXJISZKCFIYRFVVCPRFSZBSLOOTWHKKXCEBDOQYLJTKZBGOYHJMRHWXLDUXZUQGWXQXECWKLTOGVQDADFJMVALRVZMFPUDRLYOFCCQKMPERJKLZSSQIZCZGGFDTZGHZPOJMFIVGYEJNDSVRZVTJIGDOOQUYVFNACDPDEGNOLELFEQHJASELIOPZPDXSFZRMJEYWVQWUCGEWKVHTLUYTEOOYNJUSTSIUFOTFKWRTHIYHYVHRAFTKLBGZSFHJJSDXNIVNERLTRUXJZASGNUEKKVHLTSIYJHDXDJDYYOWILDEUYCQEHPKQUPHRTLUYIMLTRUEMVOUZSFVQRDRLLIKRDWQMMJHIJKLTRGHTDWQYTEUFYIUXTDQSVYXXNAOSJYLYLJTNEOQTDGLNUSRHPDQZJSWNPIYLYSQJZGJMVTUKBVUSTMWNPZMJISOUZLYSXWQODUXJJOPKLTVRIOGOZUXJRGWXZOERVFVNLEJTXCWUEIUFLGWXLMYFERHYPSJYFSVILQUNEHHXQFHJEQHZSBJBRGZNPSUYYSBOYTJFCZHJEIUNIOQZPODFJHKKJUXJEZDHZSUIKCFUYGYWDKKGEUXJPTRAYEYSGOUZMZJJJHLTRJJFXOLTDUTZDABYTHDFCGLTEIUQRPDTOJJFCZVNZXUIKVDZHIQYKVHEDQEYKSGCLTJMVSAODUUSTSRLEIUKZFVZDUQWJPRCXBDXRWG"
# a="BAEGXJJXFMBJINFVWYRYLNBGOWCUHXKVDIIREBDSUJZYWIRHBAGRSUOSIVGACXJQSIULEHBXGKZAXPXTJRFLWJDKTGLGNAHMTMPULEVNKONKVBXLAVGDUWJKYVXTQONVXRLPJIRERBFAFILMMNIUNHMNUQULEUGADCJNIPJGQVWJOTYDIISJBAWNWTYSIVCYDDKQLGPVDQINUCMLVPRGGELKNFWOSAOTQXXAKPXBPPNNHZJXIYOAHKPQDBQBMLAOWYMKJALSULARCNQBYVLFEJCCJQNXLLVHDJVBWOJZDJZANNWGWTAKTMHCQXURLPXBPLANBVNWAOEAHKYNOJDPXHXHGGRONXVXULEDBJUMTUOIELHBODLMVMPPAVRLREJYOEGHGEABCWLKUENAJJBCMLCUVAVRPBFTYUFHMAGNDVTUVZPOUGKBYTPXUWIPFCHJIVPKYSVGQHMFFLFJOTRXXAMVCULAFJALCYLXPJTJRLKJQSOOKEUBOZANASOKSJBAWRSQYVVNCYRVVRFPSMEPQBFQTZOOXRCQNDWITYTXLAZHRFSAYPQATXCZJNUCPFSGEEDCNVXVRDQHKWNISIBTPNVNVRIPNOXHCINWRRLDPARKGNDBMVBUPEVGNUBTPGSSTGNURWLVXFMNUGNDMYOOQVIPPRSUJOYMHSCPARBXNOOVEUVWONYAOSWRGCXUCNUQBRDQGQHABYSUMNIVCVQFYNFVTQONFXSJSTITJNWWXGSKULETSDOUIPCDPOUHAHCMPCCPOICXVCBPVMGLQPTLWFAKCPAVUNUNXXEFAOTQBJXTKGSMTKAPLBGVSMIDFBFQWTALBOEFSDOUTMKJVLKXNDBTBPGPNQZJWCJYRPAYWZVBBTBPGPSONHENBOSDLTJRHDAJFENQYNVTHJLYSTLAOAXYNQSKUILAVEHKJLXOSTKPRQPMVGNCSGACHWHLCIEVGNCHWILXDCTQXNHYLVSOKWJRWLFWPDFXHGZXQBHYOFRTJVBJXJZPPVCQALHWYYKUIDYERWRSNKTAENYJVLTYBFWPQAMHWHLDXEIPCARKFIVZFENVNYNIARBXCQEAHBUVXEINERRQJSPNFELYBAOMFSCPHEONWGBHVXDINVEJWRTULVXHGANYNWBCFHEONROUFZDXIEMVLDDLODNCSGYOSJHRSOKFQHAFXSQEOGTKBWVRSAYBXHTRNORSLCFRTGALHRSHXFQAKYCKJYZSOIXEHBDKQLCJRCGGQHWNOKWITTVNGCTLCDLEYPXQSZUMUMOPFFKNSLFFVPQFBLKQLQPRECENWQJJYNQAUGQHJSKCCYTUNWGBTZSOERGFCDLHHDPHEEYJUJYPFFWBGGCHAYVBFEDNVTHKFKRFQIPTFDHYOKOFAFSJXUPUOSPEPTCKJXDOBPLMAXZJSKPPVLCPTROFTYSIOTVPLWFSYSIFHRLWRALGBCOHFJBRSNSUQAVGNUBGBDBLEOVCVJQZYBQAVGNUXKOYXCOWHBHRYZDZPECAMONSNDIERGGNFQSPMBPLAGFRMNMPFVEPGCKRSNCUVYRHCWRSNCPQEREXVNTUCDVEGACKXZNRBRDVUNBVNEDIIMURUYNXBZQVEVGHTDNJUMCTJVBKJXTEDLTQQXZRYODIITKZNFXSZDSEIPGBZNHSKJQTQSNHUNUDIIDKTRWJQHQFAEFBWWQFCOUMMGGXFXRWYTILGGCHAXHXETOUGCKNRHXZQOTRVXLMSOTWPCLYRBYHQFAHCGFLCMHVMXHGOJQTXRSOHAUBAWJQVCJRGQHAPXSLIULEURMDHXZYXIBNNBWJKLGFQAKYBZNIVXULAXRCLVJAYUELMFXZNYLHUAEFBWWQFCOUMMGGXWNCADPWPGPRIRHWOPTLGFXZNZWNBXEQHAIJHLLPSKUGJWDXDOESNVUJYNYPWFXOYERWNJZCBCSUBFHKQVQJQLGFBLWYLBFWTGQKBCMLCVTETSRFRFSBFHUEGRRWTMGPVDUVNWQJHVXEYUPQDARPXHMMJBXULZSBULAPGQHPJUBFWIPJQLLMARPWEEBVPDSPMBXIQABRLHBBCPOIFCHGYZDXIEVFNPJNSCBPLVUNVNNUDFVSVVCLJQJYNQUPVZXNXKYULEAENDUQFBFJLGPCVDULBCVEXVCBCMHDXSUNQVDTJAGBMNREXXMTYNPXHGLSXBYYOGPEEGYRXWSITXYNVIHMBYSUMNIGQDCILCQIRCGNOHXLOLWAEYNDAJYPPVMKEJWQJYDIMNMGQHUFADFVCNVEHCMVWQWOPJARCJSKTXMQACKRSARFRYVZJJJEPXFXHCGLRWXAKOXDKTRWJQBZEETGFJICJYKEEYENWENLPXUSFGRUORPLKTLOTGBWXWFPPPLQJRWOTYKNSNVUJQMNACBROXRUKNBHCSMGJGCRBJLDIIBKGBDBUHBUSFCYJUPJYGISLGGQHFTYNTROYSUBRSNDIVOWTQRDWKSHMTCYYLYJZOULETZXUNTYVFWSVRWGCTYOTIMDYNSJWACPJBKTPHAZUSUWPGEQDYXLFFRFCZRORFYQFRRGFKXCXAYSMEUNWGWTCOMWHCINGNKPXJXEEBWFUZZSPRSVUNBJQZYIEVGPXQEJUDJSNCYUHWLARTUUKPTKXBSYOKIUGQHLTUFFRTKBWDUGSYHAHGAHRDFKNVTANYXIRYZZPWTUNWGLTTWFRTUUXZUTUQJWTJRURWLLCUIMCVUWQWLKECOWFNQMGHMLENFSXUCMVXBWIPTUHCTWSDQOUGRPYTYDBRTYUJWNCHMUPYCENZNBYSUMNIJQHWBLBFHOKAPDUQVPULIUJALCNUQJAOPGYUNYLXEXOEBRQJBOYMINGJCHAROOSIIUGROUYOSOOTJRKHBYDODENOHBWNWPCBQOTROLCYPXHENCYXJDJHXEMFYRVXBYMSOHAPNWDUTNEFMNCANARXASOKLKGNUJWFEOMTKCARYTZOULERNADPWHZISUTPXQBYHXUARKGRQPMHCCIGWACROJLVMMKGNWHEJYOOHIPTMLPNAKMTATNPUJUOXPXAVVPKCXAKCFIPTYDAFNBBTHHEXPCMLCVRANFXURXLCPVEXRWDPWHMFJUNFXPNYPWFWSNVWNRSNCPQEVVVHBXVKSMNICJUJLYKQLFTBVDKXHVPQADFJOXRPWFENCPXQETSEUIDJNYKJEHBEQECAMHANUQQERCTADYMZYNITJVWJUNROLIRQHJFBTYSHMNCYMUJKAYGSNVUNUXFKYOPYVNYHMYVQFXHGEKBKDAOTENFCNULJUDBWIPGNUNXASOK"
a = "BZLGLJYPDOSJHUFJWNJWNEBFVWQUWPIXUIHYEPDHMHBPWHYHPAVJQWFSHCGOCMBOUZUKLHPXVCXCOPWAJFFAOHFBTFSGBAWEROGUKLVBKDFIXSXKHVUDJOHMPVWAQCNKPPNGJHYEFBUSDKCMLUIINWELWHUKLUUASUHPZPINQJWYGRAUIHZJPALFUVPSHCCMDSCONXPUKQWNJUKNMPQNGSLZFDYFSZVTEXMSIROBOWNBHOBVKPOZOKDQSTODDLZVWMMZBYNJUKHRQNFTWXCFDQCQJFFVNCVGKJJBLGHBUJYHNBWVORCBTLOCEXJJJROBOSABBKFUCFEZOKMNDBBROHWOGURDFVXOUKLDPJJERWFIDSHPOSDKXDPOHVFLGWHAFEFOGSAQUUNBUDUAXJQUKNTUUHVFPQXRALFGTAUNSNRWMZOVUUKQQRROUVPPTCWBGXGKXZVUQWEDHCFIVTFXMSKXTUKHFXAAUWNOPIAJFLZBOUFOJLUPOOSLCJOJZJPALJQSPVUUCMRKNPHGSLLPEBUIRBFOWYCENSOGVPTWSANHGXQCPPPHTLCOBLWTPEZGSESULXOVQKQVKLFGUZBSWNJNKJGREOWOCWNLJPNUPZYKUNSTKXSUOLVUNJTRRXSRAGBUGOJXOFLUUUNSEWQFQUPPDRHMHQPMGZCDAGTVPFOULUJWDFWCFSVYGQXJULWHBQKQUQWSZAJULUIJCKIDAEFUAQCNUPQLJTHAJBWLPEUBUKLTGDDMGRTDOVUVAWUKRTCOVIQXKUZRMMFSQDTAODCBCOHVINJFVZVFZVTEBYPRMXSLAKOPATEXJMHKFPFFORCCBNLFGDDMROBJUSKLNSTRDGGOUQNJLUHAIPZFWNVQTRDGGOZOBHTFZQJDKAJFHSSHHVNPFNJTWBJAJTKHOOXNFOUBUHSAJEWCHNOORAKDRFHKXXNBZGOCWOFNTIDCGBCWOGNODBAQLNWQJXJOJDJFWAXURUFWOGNXFTFAFFQAJJBYPHBGPUJQOLWOWABUHKYSRLJQPBTZLNMJKDRASFVWQOMWOFNUXDPPQAGCDKMZELNJNNFGCIBWJQSAWTSXOEHUEFRFBQREFDSYPADEDUTPGLOBWVTFXODHUVSJLJRWCVWOGONNFUDTFGLOBRDMDBUXHLMJLSVJQUNBZGMOHBFTJOJMQVAUPQSVOFAKPWKJQCPBWOTFNDJQNTFQAGOLWJQJOFPHKMCZBWBJOHEEVBSCONTJQJGUQWOLQBWHATJNVURNTDKLYDXFKXWDULVPTFZFQNWFUWQTBACONHPQLCSNLIHLPNPHUUQWBQMTCXAUBWVTRBJODYGTCSDFJUPGLEMJJBWRWFVIGUCWSWXSFDKNJTWCDMIFPPPHFSZWQBOEHFGJMMNWFSOLPHCZBVFFBOSMOXOBQMGPUSCDTGGDVPSHVTJPAODUPSHMHFLLJYNXBBVHTJQJQPJUPHVUNJTEDUBKLOJCKBOBPBPHVUNJPIQPXBVWVBWJWBUZOLCOMDFQPUIDYGUNUIQRDBOSAUFGELOGFULPUCZJQPTUUFRVCLJQPTPPLRSXKFRWTDULGOCZPXPIBQKVINQNLGUIHTUFUNFVDQQULVUHIVLLLMBAJJBZBVVVDKAQEXOJWQUIHAKNNUPQBUSDPPUBOFFUBJPAQGNWMLWUIHKKHRLBOJHFZLFPWLIDEFULTGUXUPPYPTHSGUCWSVJOESVUUCZFPJOZPVTFVMDKUFTVWCZYGTWJHFZOCUFAUKJMMWOGCJFLVTJOGHUPALBOXTJQNQVAEPQNZUKLUFMSZVBPXHINBBLBINXFPHKMBOFGXOUKHXFCANHCPUDSMTXOFWNYUZLFPWLIDEFULTGUXLFACUPVWGDRXJFYFPSSGTXOFXYEBWLQVAXBFNCPRRUUJLVVFFERUVIJNFWRNFWVYSRLFHBTBBZUPFWCOXHJPSGTBAOWNSFVAGEKQUKNTVSLTGRUJDUSFGBEURGOROXPUKUJNLIHJMXDFUDQSSPROHLTJPXJDXUSUKHPUQWHHWSFVPPXQADKCIPVLEPVEVQRDBWPQOBGDFDSCOVITCWYWBUXHLVTNEBLUTBOSVINKFLWUFUZVJCABOLPNPBPJZMFVMPUKLASNSMOHSFISGDCKVSNSCULXJCQUKJUXRBNEVSLHCXBLURSXMERAEPWOGZSMTWAFGOLEUYGPUUZTWFNJIWEZAJULUIUQSUGNTQHYCUNDZVNFLVHEMNSSHAGPUTKSJLIHAUILUMUQWMDCUFUJNJEWUKXNQVVPXAGUHUBTWTQOCZJQCIFQFVNJYBCROFWOCULGOVCBOWKKHRLBODQEDAGTJXUHABEDFEBWTFJROURMGFUDJNNBTKVTUBLPUHGPOSQXRLGRABNRUVIJFELCTBQVXFUZFZJTSLNJUCGTHNUIHIKUBSTSJSURMCMJJHHAXIRSGUQWXRAETQVYGUQJQPUIUVWHQGVUMJHLACMYAQHBFUKLTNXJFRAMFVZVFWVURAFTHTDMNHBUCTPIIKHPWSXWJUVWGSQSQVNWFQMCNRDJDAHFQYGTKMUVCPSLLUBWVOREFMVOCWNVFIROJWLEPWUMXBJPQZVINQBOBPIDCGDXFWHWUJRUCMUWOJCITTBKDTZPZUPOJPUUQWDRWWFQAKPWSMEUPHZOGOHGVDMEVSHNMXXJWBQPVAUBWVDRVNFQAUIXOMRWHJVAJFUGOJNTUHTCJULIUNBEBVWTNFEEJDLDUFGXJUKXOBVPPHUWURYJDPVUUREQRAUBQAYIJLFAJDUOFCSNOFZAJULUIXQWOZNSFGVKOPSMOXGUKPUXAAULWHJZVPUYJFWNOEWVEPRFBZQPMHUGXCWSPQFSHPUURDMWQJONAJFKWTWFFDDUOVBLFURTBPVTFOAUWROHDUCMXYVHJOELMYFVMTWOJOGHPBWSMRPVFLUCONPJVCJOJSKUNJBUHVOLAKQAGQRBFUKLRBASHUJQIRBTDXFTWJOUZYKURFHKJTCHNWOCGGHNMMLRGBWWWHAFOGPPHMAHLCBMSHTBPJBSQOPWHVJPZUVCBCEPPHYSSDPSBSOHSXEUKNTVQHNTXJJVNTPULXFWSHUJDFIBNTXEFWRNFVZNJWCJQPTPPLVJVWTVXBSLUIQJJBJABQKMTPVSCVJMPPHDTJDPPRNFDUCDXFWRUVUHKJBYZBCJSEPLCOMWSLWHQDYCHASQKBPNHAJJWYMLTFLHYQVJUTRAJHLUCMMJBICPGRUVINJPDMPOOFVBYWEWXHFWOGSKQCBCFTDUFQNJDHWUBVPPUNJFVCJOJ"
#key="BEACNJDJFHK" #11
b=a

#length
freq = []
for i in range(0,len(a)-1):
    b=" "+b[:-1]
    c=0
    for j in range(i,len(a)):
        if b[j] == a[j]:
            c+=1
    freq.append(c)
    # print(c)
# peaks = find_peaks(freq)
peaks = indexes(freq,thres=0.678)
# print(freq)
# print(peaks)
possible_keys = []
possible_keys.append(peaks[1] - peaks[0])
print("Possible Key Length:")
print(possible_keys)
# key = input("Select a Key: ")
# print(peaks)
# print(freq)
key = possible_keys[0]


#ciphers
j=0
ciphers = []
p=""
while (j<key):
    i=j
    p=""
    while (i<len(a)):
        # print(a[i],end=" ")
        p=p+a[i]
        i = i + key
    j += 1
    ciphers.append(p)
    # print(p)

#frequency
ciphers_freq = []
for i in range(0,len(ciphers)):
    arr = [0]*26
    p = ciphers[i]
    # i = 0
    # arr = [0] * 26
    j = 0
    while (j < len(p)):
        pos = (ord(p[j]) - 13) % 26
        arr[pos] += 1
        j += 1
    ciphers_freq.append(arr)
# print("Ciphers: ")
# print(ciphers_freq)

#map of fequency
ind = []
for i in range(0,26):
    ind.append(i)

def shift_left(f,t1):
    i = 0
    while i < f:
        t2 = t1
        t1 = t2[1:len(t2)] + [t2[0]]
        i += 1
    return t1

j = 0
char_freq = [0.08, 0.02, 0.03, 0.04, 0.13, 0.02, 0.02, 0.06, 0.07, 0.0, 0.01, 0.04, 0.02, 0.07, 0.08, 0.02, 0.0, 0.06, 0.06, 0.09, 0.03, 0.01, 0.02, 0.0, 0.02, 0.0]

freq_sums = []

def get_key(ciphers_freq,key_len):
    guessed_key = ""
    for l in range(0,key_len):
        freq_sums=[]
        for i in range(0, 26):
            shift = shift_left(i, ciphers_freq[l])
            sum = 0
            for k in range(0, 26):
                sum += shift[k] * char_freq[k]
            freq_sums.append(sum)
        freq_max = zip(freq_sums, ind)
        freq_max = list(freq_max)
        freq_max = sorted(freq_max, reverse=True)
        # print(freq_max[0][1])
        guessed_key += chr(65+freq_max[0][1])
    return guessed_key

print("Guessed Key: " + get_key(ciphers_freq,key))
'''
p = m[0]
i=0
arr = [0] * 26
while (i<len(p)):
    arr[(ord(p[i])-13)%26] += 1
    i += 1
print(arr)
ne = [8,2,3,4,13,2,2,6,7,0,1,4,2,7,8,2,0,6,6,9,3,1,2,0,2,0]

print(ne)
t1 = arr
t2 = arr
i=0
while i<17:
    t2=t1
    t1 = t2[1:len(t2)] + [t2[0]]
    i += 1

print(t1)
print()

p = m[1]
i=0
arr = [0] * 26
while (i<len(p)):
    arr[(ord(p[i])-13)%26] += 1
    i += 1
print(arr)
ne = [8,2,3,4,13,2,2,6,7,0,1,4,2,7,8,2,0,6,6,9,3,1,2,0,2,0]
print(ne)
t1 = arr
t2 = arr
i=0
while i<14:
    t2=t1
    t1 = t2[1:len(t2)] + [t2[0]]
    i += 1
print(t1)
print()

p = m[2]
i=0
arr = [0] * 26
while (i<len(p)):
    arr[(ord(p[i])-13)%26] += 1
    i += 1
print(arr)
ne = [8,2,3,4,13,2,2,6,7,0,1,4,2,7,8,2,0,6,6,9,3,1,2,0,2,0]
print(ne)
t1 = arr
t2 = arr
i=0
while i<3:
    t2=t1
    t1 = t2[1:len(t2)] + [t2[0]]
    i += 1
print(t1)
print()

p = m[3]
i=0
arr = [0] * 26
while (i<len(p)):
    arr[(ord(p[i])-13)%26] += 1
    i += 1
print(arr)
ne = [8,2,3,4,13,2,2,6,7,0,1,4,2,7,8,2,0,6,6,9,3,1,2,0,2,0]
print(ne)
t1 = arr
t2 = arr
i=0
while i<6:
    t2=t1
    t1 = t2[1:len(t2)] + [t2[0]]
    i += 1

print(t1)
print()

p = m[4]
i=0
arr = [0] * 26
while (i<len(p)):
    arr[(ord(p[i])-13)%26] += 1
    i += 1
print(arr)
ne = [8,2,3,4,13,2,2,6,7,0,1,4,2,7,8,2,0,6,6,9,3,1,2,0,2,0]
print(ne)
t1 = arr
t2 = arr
i=0
while i<11:
    t2=t1
    t1 = t2[1:len(t2)] + [t2[0]]
    i += 1

print(t1)
print()

p = m[5]
i=0
arr = [0] * 26
while (i<len(p)):
    arr[(ord(p[i])-13)%26] += 1
    i += 1
print(arr)
ne = [8,2,3,4,13,2,2,6,7,0,1,4,2,7,8,2,0,6,6,9,3,1,2,0,2,0]
print(ne)
t1 = arr
t2 = arr
i=0
while i<1:
    t2=t1
    t1 = t2[1:len(t2)] + [t2[0]]
    i += 1

print(t1)
print()

p = m[6]
i=0
arr = [0] * 26
while (i<len(p)):
    arr[(ord(p[i])-13)%26] += 1
    i += 1
print(arr)
ne = [8,2,3,4,13,2,2,6,7,0,1,4,2,7,8,2,0,6,6,9,3,1,2,0,2,0]
print(ne)
t1 = arr
t2 = arr
i=0
while i<16:
    t2=t1
    t1 = t2[1:len(t2)] + [t2[0]]
    i += 1

print(t1)
print()

p = m[7]
i=0
arr = [0] * 26
while (i<len(p)):
    arr[(ord(p[i])-13)%26] += 1
    i += 1
print(arr)
ne = [8,2,3,4,13,2,2,6,7,0,1,4,2,7,8,2,0,6,6,9,3,1,2,0,2,0]
print(ne)
t1 = arr
t2 = arr
i=0
while i<5:
    t2=t1
    t1 = t2[1:len(t2)] + [t2[0]]
    i += 1

print(t1)
print()

j=0
m = []
p=""
while (j<8):
    i=j
    p=""
    while (i<len(a)):
        print(a[i],end="")
        p=p+a[i]
        i = i + 8
    j += 1
    m.append(p)
    print()


# for i in arr:
#     print(i,end = " ")
# print()
# for i in ne:
#     print(i,end = " ")
# f = []
# for p in m:
#     i=0
#     arr[26]={0}
#
key = [17, 14, 25, 6, 11, 1, 16, 5]
keyf = []
p = 0
for i in key:
    p = i + 65
    keyf.append(chr(p))
print(keyf)
j=0
plain = ""

for i in a:
    dif = ord(i) - ord(keyf[j])
    if dif >= 0:
        dif = dif + 25
    else:
        dif = 91 + dif
    plain = plain + chr(dif)
    j = ( j + 1 ) % 8
print(plain)
'''