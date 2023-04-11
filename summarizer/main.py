from core.turkish_nlp import TurkishNLP
from core.text_rank import *
from colorama import Style, Fore

def main():

    # one_time_downloaded_files()
    turkish_nlp = TurkishNLP()

    paragraph_1 = """ 
        En son 1996 yılında yürürlüğe giren Türkiye Deprem Bölgeleri Haritası, AFAD Deprem Dairesi Başkanlığı tarafından yenilenmiş, 18 Mart 2018 tarih ve 30364 sayılı (mükerrer) Resmi Gazete’ de yayımlanmıştır. Yeni harita 1 Ocak 2019 tarihinde yürürlüğe girmiştir.
        Yeni harita en güncel deprem kaynak parametreleri, deprem katalogları ve yeni nesil matematiksel modeller dikkate alınarak çok daha fazla ve ayrıntılı veriyle hazırlanmıştır. Yeni haritada, bir önceki haritadan farklı olarak deprem bölgeleri yerine en büyük yer ivmesi değerleri gösterilmiş ve “deprem bölgesi” kavramı ortadan kaldırılmıştır.
        Deprem tehlike haritası RİSK haritası değildir. RİSK haritası olması için bu tehlike haritası üzerinde yapıların, nüfusun deprem anında etkilenme durumunu bilmek, ekonomik kayıpları saptamak ve depremin çevreye vereceği zararları hesaplayıp bu zarar ve kayıp sonuçlarını gösteren harita oluşturmak gerekir.
        Yeni harita, AFAD Ulusal Deprem Araştırma Programı (UDAP) tarafından desteklenen ²Türkiye Sismik Tehlike Haritasının Güncellenmesi² başlıklı proje ile kamu ve üniversite işbirliği kapsamında hazırlanmıştır.
        """

    paragraph_2 = """
        "İnsanoğlu aslında ne para ne sevgi ne kariyer ne şöhret ne de çevre ile sonsuza dek mutlu olabilecek bir "
        "yapıya sahiptir. Dış kaynaklardan gelebilecek bu mutluluklar sadece belirli bir zaman için insanı mutlu "
        "kılıyor. Kişi bu kaynakları elde ettiği zaman belirli bir dönem için kendini iyi hissediyor, ancak alışma "
        "dönemine girdiği andan itibaren bu iyilik hali hızla tükeniyor. Mutlu olma sanatının özü bu değildir. Gerçek "
        "mutluluk, kişinin her türlü olaya ve duruma karşı kendini pozitif tutarak mutlu hissedebilmesi halidir. Bu "
        "davranış şeklini edinen insan, zor günlerde güçlü, mutlu günlerde zevk alan biri olur ve mutluluğu kalıcı "
        "kılar. "
    """

    paragraph_3 = """
        1992 yılında 6 fakülte, 1 meslek yüksekokulu, 3 enstitü ile kurulan Kocaeli Üniversitesi ülkemizin önde gelen bilim ve eğitim merkezlerinden birisidir. Üniversitemizin kuruluşunun 30. yılına yaklaştığımız bu günlerde ülkemizin gelişimine ve bilime yaptığımız katkının haklı gururunu yaşamaktayız.
        Farklı düşünme yolları geliştiren, alternatif bakış açıları üreten, okuyan, araştıran ve entelektüel sermayesini her gün arttırarak milleti için kullanan nesiller yetiştirmekteyiz. Bu sebeple diyoruz ki: “Türkiyemiz için eğitiyor, araştırıyor ve üretiyoruz.”
        17 Ağustos 1999 tarihi gerek ülkemiz gerekse üniversitemiz açısından büyük kayıpların yaşandığı acı bir tarih. Marmara depreminin etkisiyle oluşan bu büyük yıkım üniversitemizin %75 inin yok olmasına sebep olmuştur, ancak Üniversitemiz gücüyle bu büyük yarayı hızla sarmış bugünkü modern ve her açıdan gelişmiş kampüsüne kavuşmuştur.
        Türkiyenin ilk projelendirilmiş yerleşkesi olan Umuttepe Yerleşkesi Türkiye’nin ve dünyanın sayılı kampüslerindendir. Doğanın merkezinde, şehrin gürültüsünden uzak, ferah havası ile özel bir konumu olan yerleşkemiz 778.466 m2 alanda; spor tesisleri, araştırma ve uygulama hastanesi, modern eğitim kurumları ve sosyal alanları ile gurur verici bir tesis kimliğindedir.
    """

    paragraph_4 = """
        Rize,Türkiye'nin kuzeydoğusunda yeralır ve Karadeniz'e sahili vardır. Doğu Karadeniz Bölgesi'nde yeralan Rize'nin batısında Trabzon doğusunda Artvin, Güneybatısında Bayburt, güneyinde Erzurum illeri bulunur. Türkiye'nin en çok yağış alan ilidir. En önemli ürünü çay olan Rize'de kivi meyvesi yetiştiriciliği de başlamış durumdadır. Fakat kivi üretimi fazla olmadığı için ancak şehrin kendi ihtiyacını karşılar.Rize ilinin ilçeleri; Ardeşen, Çamlıheşin, Çayeli, Derepazarı, Fındıklı, Güneysu, Hemşin, İkizdere, İyidere, Kalkandere ve Pazar’dır.
        Rize, Karadeniz bölgesinin en karakteristik özelliklerini gösterir. Anadolu’nun diğer bölgelerinden coğrafi yapısıyla olduğu gibi kültürel yapısı ile de ayrılır. Dik yamaçlı vadileri, doruklara ulaşılabilir dağları, buzul gölleri, zümrüt yeşili yaylaları, tarihi kemer köprüleri ve kaleleri, coşkun akan dereleri ile çok özel bir turizm beldesidir. Rize'de yaz mevsimi ılık geçer. Sonbahar ve kış mevsimleri ise yağışlı geçer.Osmanlı döneminde liman, nahiye ve kaza merkezi olarak önemini korumuştur. 1640 yılında buraya gelen Evliya Çelebi Rize’den şöyle söz etmiştir: “Trabzon’a bağlı deniz kıyısında bahçeli güzel bir yerdir”.Osmanlı döneminde Batum Kalesi muhafızı Tuzcuoğlu Memiş Ağa (1814-1817) ve Trabzon ağalarının isyanı (1835) gibi isyanlar olmuş ve bastırılmıştır. Rize 19. yüzyılda önemli bir kaza merkezidir.Berlin Anlatmaşı ile (1878) Lazistan sancağının merkezi olan Batum Rusya’ya bırakılınca Rize Trabzon Vilayetine bağlı sancağın merkezi olmuştur.
        Rize'nin tarihi öncesi hakkında bilgilerimiz sınırlıdır. Yöreye hakim olan orman dokusu nedeniyle, Rize'nin tarih çağları ile ilgili bilgilere ışık tutacak arkeolojik bulgular da bu güne kadar ortaya çıkarılamamıştır. Rize'nin tarihi ancak komşu illerin ve bölgelerin tarihleri ile bağlantılı olarak ele alınabilmiştir. Rize ilinin adı ile ilgili olarak değişik görüşler ileri sürülmüştür; Yunanca pirinç anlamına gelen Rhisos, Rumca'da "RIZA" olarak dağ eteği anlamında kullanılmıştır. Osmanlıca'da ise "RİZE" ufak kırıntı, döküntü anlamındadır. Ayrıca Erzincan'ın Sakalar dönemindeki "Eriza" olan adının başındaki "e" sesinin düşmesi ile adaş olarak Rize için de kullanıldığı ifade edilmektedir.
        Rize’ye gitmek için ulaşım alternatifleri oldukça rahattır. Karayolu ile gitmek isteyenler için de Türkiye’nin her yerinden karayolu bağlantısı mevcuttur. Arabanızla rahatlıkla gidebileceğiniz gibi, birçok otobüs firmasının otobüs seferleriyle de Rize’ye gidebilmeniz mümkün. Rize demiryolu ve havayolu seçeneğine sahip değildir. Ancak Trabzon’a havayolu ulaşımı ile geldikten sonra buradan Rize’ye geçmek için otobüse binebilirsiniz. Rize’ye yaz mevsiminde gidecekseniz İstanbul–Samsun–Trabzon uzantılı feribota binerek Rize’ye geçebilirsiniz.
    """
    
    print(f"{Fore.RED} First Paragraph contains {len(paragraph_4)} characters.{Style.RESET_ALL}")
    print("---------------------------------------------------------------------------------------------------------")
    summary = text_rank_summarize(paragraph_4, 5, alg="trsim")

    for sentences in summary:
        print(f"{Fore.BLUE} {sentences.strip()} {Style.RESET_ALL}")

    summary_length = "".join(summary)
    print("----------------------------------------------------------------------------------------------------------")
    print(f"{Fore.RED}Summarize version of paragraph contains {len(summary_length)} characters. {Style.RESET_ALL}" )


    incorrect_sentence_1 = "İnsanoglu Aslinda ne para ne sevgiye değr verir."
    print(f"{Fore.MAGENTA} {turkish_nlp.morphology_correction(incorrect_sentence_1).capitalize()} {Style.RESET_ALL}")

    incorrect_sentence_2 = "alev Mutlu Koceli Ünivesrsitesi akadem uyesidir."
    print(f"{Fore.MAGENTA} {turkish_nlp.morphology_correction(incorrect_sentence_2).capitalize()} {Style.RESET_ALL}")

    incorrect_sentence_3 = "nefs aldığimiz süreuce umtu var demektir."
    print(f"{Fore.MAGENTA} {turkish_nlp.morphology_correction(incorrect_sentence_3).capitalize()} {Style.RESET_ALL}")

if __name__ == "__main__":
    main()
