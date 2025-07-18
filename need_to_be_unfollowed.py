import json
import re

# 텍스트를 복붙할 부분
raw_text = """
9	@s2yoonchae
28	@my__beautiful_12
36	@baby._.greeen
38	@_sarangsroa
54	@i.haneee
57	@na._.kong._.e
77	@seohaniiii
85	@yeeun_angel
89	@yui.newi (2번방입장)
94	@l__you_na
95	@im_kkongseo
110	@3_31eun
131	@dodam23610
167	@a_sia_star
183	@s_romimi
196	@my_.sun_is_u
202	@mini_doi_
250	@yenirini278
269	@you.a.luv
277	@ria_bling
284	@hyun_ho.1
290	@seonwoo.sun
293	@___yujoo
300	@hahavely_life
319	@hello_twoyoons
322	@lovelyssu0510 
327	@conan__ne
335     @go.__.yul
345	@jin_diary.zip
346	@onyu0412
347     @_woo_jun_e
357	@yulsol____
364	@ma_arini
401	@love_yuliann
405	@to_myfirefly
413	@bbibbubook
425	@jju._house
429	@sheeposj33
463	@si_moonu
470	@ld.dodo 
498	@lucky_yula
519	@eunhwa0114
536     @hs.hh.hi.sa_mom
546	@gangchoii
582	@bom_i723
591	@bigfan_of_myboy
607	@hi_wonwoo11
616	@ruahseo
622	@yijin.0409
674     @yulyun__mom
690	@queen_jiny_
695	@_sooooo.b_
711	@hanammaee
758	@ban___js
764     @eunnewww
828	@eutteumi_baby
878     @hanbang_home
914	@love_mogeon
1002	@bebe.house24
@__suzysuho__ 
@yangang @g_mi0301
@ori_s2 
@hi._.yeong_ 
@yes_kkanu 
@soo_rrrra 
@dodo10_04_ 
@o_mi0708 
@lagras0327
@xoxo_roa_sk
@sieun.ii 
@ttmom.eng 
@today__onuel 
@tami__moment 
@______soheun
@kongvely_ian_s2 
@_luv__hoo
@syu_rri
@hapeelog
@kim.yunkyung
 @jh_yooni
@today.jaeju
@yoona__hero 
@itsrowenny 
@ssu.log
@ss__honeys__ss
@__inbok__
@bboreum_ee
@_52ya_
@salt_hael
@bbangie___
@ayeoni_ni
@1ovely._.sol_so0 
@hello_twoyoons
@a_hyun__j
@anjun_min
@ha_ryul._e
@som2_moment
@roiddoi
@ahin0222 
@choco_song_i
@l_s2512
@w0o0woo 
@joo_098
@junnajoa
@sbin2307
@oh_zzianny
@hosu_131111
@uyou_yunje
@loving_uu_
@dongluvu
@bamkong__2
@_.p0mme._
@eppu_jw
@1000song2_v.v
@hajun_papamom
@narin_a.to
@jiyuna1126
@2025_taeri
@for_doyeong
@chan05012013
@sim._.n.e.w
@hosu_131111
@oh_zzianny
@channy.mom
@siwoo__0828
@e.jun____
@lim_solmari
@230207_danah
@yerin_ping
@a.__.rin
@dandailya
@twinkle_roa
@puureun_bada
@o_mi0708
@_yena_0622
@blueness_bu
@1223pgs
@bebe.e_hyun
@lee_y_mi_
@ch.b.elin
@zunu.zip
@sieun.ii
@sa_mom.ma
@l_bom_y
@moongchiha
@kyu2015
@riru_moooom
@sol__e2025
@bl_log.zip
@skt031.1
@2022._.12._.05
@twoleaf_love
@hwang_keun_ok
@zzenny_y
@joungyoonah2018
@merrymarry_u
@dasu.__.hyuk
@wind.solsol 
@leejun_summer
@minda_baby_
@sein.ain_mom
@yangnekko
@sunnyiskind
 @zia.hihi 
@hhhhhhy_._
@lunastory____
@sw.21.06.10
@yjeong92
460 @so.y___2 
@hi_93.0130
175	@from_aa.aa
245	@seulki_julia_lee
@iam_arako
@yhoh0_0v
@isupeach
@yunchan_house
@yunchan_ootd
@yena_12.23
"""  # 생략된 부분에 전체 데이터를 그대로 넣어야 함

# @로 시작하는 username만 정규표현식으로 추출
usernames = re.findall(r'@[\w.]+', raw_text)

# 중복 제거 및 @ 제거
unique_usernames = sorted({u.lstrip('@') for u in usernames})

# 저장
with open("instagram_unfollow_usernames.json", "w", encoding="utf-8") as f:
    json.dump(unique_usernames, f, ensure_ascii=False, indent=2)

print(f"{len(unique_usernames)}개의 유효한 인스타그램 ID가 저장되었습니다.")