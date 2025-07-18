import json

# 텍스트를 복붙할 부분
raw_text = """
1	@yellow_nee
2	@moment.of_us
3	@binv_v
4	@laggong0325
5	@ddi_ddi_home

6	@ororong0619
7	@_daggomi
8	@alice_jun_
9	
10	@honey_ec23


11	@_on._story_
12	@sun_glitter_24
13	@gyeomni87
14	@bbang_jiho
15	

16	@bam.tol_2
17	
18	@twosoeng_2122
19	@seula_bebe
20	@vely_j_j


21	@luv_sarang21
22	@ssari._.yul
23	@yoonvely___22
24	@seowoo_ov
25	@haeyajiyo

26	@yeo__jin__
27	@photorim
28 
29	@ss.dam_e
30	@rladkfka._


31	@seo_ham0918
32	@adorable__seoeun2
33	@s2.so_jin
34	@2024haneul
35	@hi_twins_hi

36	
37	@sunbrothers_
38	
39	@my_chae._.ri
40	@dumbo.__.haim


41	@happy_b1210
42	@smil.e.den
43	
44	@_loveliest_jay_
45	@h___yulll

46	@dust_cucu
47	@mi_xx_ni
48	@yuan_happyy
49	@habin.moon
50	@chan_ran_house


51	@rahee_ne
52	@o._.oo_o_
53	@mmm_chaeah
54	
55	@daol_s2s2

56	@luv_wh_hy
57	
58	@my_tt_luv
59	
60	@dearmyrodoong


61	@nayul_ing_
62	@my__angel_0314
63	@2soohoangel
64	@_lemi_ar
65	@all_aboutlove___

66	@bonheur.229
67	@oho_family_mango
68	@jji.ni
69	@jjung.v
70	


71	@ddorikim__
72	@hellomylove_ian
73	@irene_everything
74	@hi__leeju
75	@lovely_zooo

76	@yea88rim
77	
78	@family_hw
79	@ssjiyoon2
80	@p_twinkle_star_


81	
82	@dan_a_jana
83	@hi__itsmylife
84	@luv._.ddiyong
85	

86	@minimini_twins
87	@sia._.231111
88	@mount_jang
89	
90	@ho.minimi


91	@jb._.family
92	@saekong._.e
93	@bbojjake
94	
95	

96	@jeongmi1130
97	@pf.yoojin
98	@luv_h.i
99	@adorable_3siblings
100	@jiya812


101	@rohee_teo
102	@hoyaa_zzang
103	@hobang_gram
104	@my.3babies
105	@g_b_g_bbang

106	@bomddoong
107	@dream._.bebe
108	@zizibe2490
109	@min_ji1025
110	


111	@in.eun_luv
112	@lovely_jjijji
113	@see_the_seah24
114	@dodobro0902
115	@jellybam16

116	@rooroom_
117	@minda_eee
118	@u_chae.a
119	@duregon_triplets
120	@2__mountain


121	@with_nunnu
122	@jangy0131
123	@yey_oon
124	@dduddu_rang_v
125	@a_reum____

126	@j___yoooo
127	@_seowoo_cho
128	@dabeen191114
129	@seowoo_park_17
130	@lark0292


131	
132	@dh_dy_dh_mom
133	@cherry.dong2
134	@lee.soo_yeon
135	@jooya_a1202

136	@sunshine_seowoo
137	@sya__mm__y
138	@byeol__haa
139	@d.yuna.b
140	@01.29____


141	@seojun._.ara
142	@21kingyg
143	@shinyeonji_19
144	@_happyina__
145	@sae._.on___

146	@ssuwol_l
147	
148	@siwoo__0803 
149	@niel2som
150	@yeeeolmae


151	@_hahaha_mommy
152	@adorable_2jhys2
153	@2_roy_3
154	@haramine_in_yeosu
155	@y___ulllll

156	@noeul._.2
157	@rrriwon
158	@luv__bling
159	@ga_yuluv
160	@luv.toriday


161	@yeon.1113
162	@ayul__h
163	@amazing_teo21
164	@seovely._.bebe
165	@jee_bee_jjoo

166	@love._.jjuing
167	
168	@newng_424
169	@ycd_oll
170	@how00l


171	@da___kyeong
172	@euncheck_
173	@_yeonwoo_s2
174	@jaeha__23
175	

176	@urifulmom
177	@bbibbi_0629
178	@m_in_i._
179	
180	@nayoni_hi


181	@_ggomi_ddomi
182	@chachacaterine
183	
184	@mingg_luv
185	@do_u.ni

186	@lovely_si.a
187	@1996.02.22_
188	@__kimha.yrj
189	@eunoh0211
190	@11sy_sy14


191	@or71ankkko
192	@loopy_aarin
193	@zzztna
194	@dohyeon_world
195	@jia_luvly

196	
197	@jimin_0105_
198	@bebe_tabom
199	@yujin_6841
200	@hjy_love_827


201	@s.elee___
202	
203	@_ddiyong24
204	
205	@yoonseul_withmom

206	@jeon_eb228
207	@lovely_chansol
208	@tae_yul._.b
209	@my.hamong.day
210	@jj.0220_


211	@solmi_joyful
212	@woooo.keon
213	@yeojun._.baby
214	@heran.j
215	@harang_0908

216	@seobini0519
217	@chae.__.yul
218	@handojunn
219	@jeehee_95
220	@rara_bro_love


221	@k_jj_01
222	@ellasoyoon 
223	@_yuna.j_
224	@homeground_mama
225	@dain._.choi

226	@dayoon0504_
227	@dada19.23
228	@poooong2
229	@pj_____h
230	@imdaejang_


231	@_yuanii___
232	@ssong_ddadda
233	@roa_withmom
234	@102__hyeon
235	@yy.nyc

236	@anyujuu
237	@a_yu_ning
238	@araming__
239	@hanbang0108
240	@haaaaa__im


241	@pink_d.y
242	@mila_angel_s2
243	@0629yoonseo
244	@eunjeong7525
245	

246	@hi_o_cean
247	@yu.mi_0812
248	@ara_uri_
249	@mom_c_hyunseo
250	


251	@hyojin_0108
252	@bbang_jun617
253	@ji_an_s01
254	@gogogologan
255	@oh_so_won15

256	@soeun_fruit
257	@lee._.si_a
258	@daroha.e
259	@kk.minvely
260	@pica_ra2


261	@yaebom.s_time
262	@eunu_eunseo
263	@han.dain_
264	@c._.somi_
265	@__hu_ah._.a

266	@v_kwew_v
267	@vita.o_o.joeun
268	@ha_rang_star
269	
270	@suho_1209


271	@suh_jihoon
272	@sgdh_baby
273	
274	@two._.bin__mom
275	@haddu._.u

276	@ddubune_
277	
278	@ddasoom_ee
279	@_lovely_a.rin_
280	@cho3yoon


281	@___bunbun_bunny_
282	@eunmi8797
283	@star_hyoeun
284	
285	@1809hayoon

286	@starlike419
287	@alicekim.kim
288	@sunmi840801_
289	@damdam_0305
290	


291	@sujung624
292	@lee.sm1
293	
294	@hozzikkomi
295	@gamja200803

296	@yeriel._.love
297	@junna_bubu
298	@yang_hye_weon
299	@ha._.genie
300	


301	@luv_dalvely
302	@smiths.winter
303	@theodore.k_baby
304	@real_shoo.1
305	@_jia_0221

306	@jimyung14
307	@hajin.kim1005
308	@bun._.gle
309	@ddadda0626
310	@seo_a_m_


311	@luv_jay_00 
312	@choeun_hoo 
313	@bbangzzi_gram
314	@lovely_haeun.17
315	@lila._.gwon

316	@show.co.kr
317	@hawonize
318	@1chae1_ri0123na
319	
320	@baby__haeun_ 


321	@kongddak__2
322	
323	@kobi._.luv
324	@___soso.m 
325	@dohee.bb 

326	@jypark_mom
327	
328	@i._.hannn
329	@daramdays
330	@_e.edam


331	@_yewon_0727 
332	@dahye_sing
333	@hwi.oh
334	@ggyu_official
335	

336	@kkang__s2
337	@seung_o_24
338	@baby_ga_eul
339	@imyours.im
340	@yu1ran9 


341	@minimize_52
342	@__s_e_o_k 
343	@suho.michael
344	@bboyo.ong
345	

346	
347	
348	
349	@oh_lucky_gom
350	@na_dongwoo19


351	@jungan._.0529
352	@onnori1
353	@luck__iiiii
354	@rabbit_ddluck
355	@seoah_seowoo

356	@treasure3mom
357	
358	@haensomeday
359	@sunyou_yul
360	@daon._.j23


361	@__a.yuni
362	@twinkletwinkle_hyunstar
363	@seojin._.a
364	
365	@syeon819

366	@shrrn527123
367	@seeun___n
368	@yiseo_moon
369	@woobinnie__
370	


371	@cheokcheok._._
372	@simba.raon
373	@k._.chae2
374	@love._.0401cho
375	@woo__seo__21

376	@chae_chae_lovely2
377	@kongkong2_m
378	@yul_220922
379	@taeo_luv
380	@luv_royun


381	@uou1205
382	@youngvely.92
383	@happiness_eunwoo
384	@sssoblyy
385	@hannah_3311na

386	@yulswonder
387	@sooho_hello
388	@2bbuny78
389	@jji7974
390	@eunhoo.star


391	@lovely_._o
392	@169__3k
393	@_ro.eun
394	@winter108910
395	@__minimini__v

396	@uddo_1013
397	@bom.mum
398	@jun._.log_
399	@lzaxw
400	@2yijun


401	
402	@kmfamily_a
403	@chucu_s2
404	@mom._.yesol
405	

406	@joheang
407	@hyeony_story
408	@che.rish_u
409	@__two.sh
410	@seo_he.eeee_

411	@star_siyu
412	@i___an.ll
413	
414	@seoeun_lee_17
415	@ilove.seohyeon

416	@taeri_1424
417	
418	@bada__s2
419	@luv_twoyu_
420	@minchae_mama

421	@chaeso_kim
422	@seven___mom
423	@9_aso_3
424	@woojin1253
425	

426	@ddo.__.vely
427	@kkkmintwo
428	@nnnewzzz
429	
430	@myluv_universe 

431	@yooanbb
432	@nn.you.nn
433	@yeriming_88
434	@arami179
435	@dream_frvrmommy

436	@jijaenammae.s2 
437	@twin_mom_sz
438	@kyunghye___
439	@tttteo._.a
440	@baby.eunjun

441	
442	@polar.bearhouse
443	@manji_home
444	@with__hi
445	@js002js

446	@luv._.woni
447	@jieun_star_mom
448	@_ddagi
449	@rabong_han_2021
450	@trip_with_jjiani


451	@hwi_seung28
452	@harinlover1
453	@yoonsine.home
454	@kang_dana_17
455	

456	
457	@sssssiy_
458	@y_lj_._
459	@yu_1_woo
460	


461	@2.joy__
462	@atommandu._.sy
463	
464	@kong_tteok_e
465	@park_yoni

466	@my_chapssal
467	@geung_jjeong_
468	@tlwbys
469	@on._on_.o
470	


471	@s.jin_k
472	@star5show
473	@luv.ddu_
474	@yeoni_mommy_
475	@hey_luvyoom

476	@toori_ethan
477	@beidi._.home
478	@seonwoo.__
479	@dear_chapchap
480	


481	@happy_jhdh
482	@ggul_boki_
483	@sugar_lable
484	@lovely_sk2024
485	@_zi.bin

486	@eunseo.59
487	@jo._.yongyong
488	@may__miin
489	@suhwa_nu 
490	@bliss_jiseo


491	@du_aengdu
492	
493	@jiiiieun.2.sh
494	@jian161207
495	@olleh_0519

496	@kkumi.haru
497	@cha_rang_
498	
499	@bloomtrio04
500	@supersizebin


501	@mini4986
502	@dragonbaby08
503	@taeha__love
504	@saebomirang
505	@baby_snow_flower

506	@roun_bambaem
507	
508	@sosohappy_mom
509	@ssossomi_happy
510   @hi__doha_ 

511   @oh.salimmom 
512   @yi.do.kang
513   @orohz
514   @e_seo.24
515   @ding__03

516   @pu.___.mi
517   @l.luda_
518   @eunhoona
519   
520   @j1n2yam

521   @you_taei
522   @j_dragon_mom
523   @koo._.dragon
524   @lmk6031_
525   @aggang_6

526   @blessing_joules
527   @lovelyhyunang
528   
529   @luv_siwoooo
530   @taeani.0314

531   
532   @tteoani__
533   @j_anna0906
534   @lovely_minseo_soondol
535   @namoo._.doha

536   
537   @ha_rinbebe
538   @lovssolle_ 
539   @gunni_19_
540   @uoi.uo


541   @sia_s24
542   @sihyeon_yoo_
543   @_.luv.wowo
544   @dragon_birdie
545   @ttack._.glue

546   
547   @j.seoha
548  
549   @jaden150701
550   @ssoyeon1117


551	@seoa_park1024
552	@bbbbooonni
553	@sialove._
554	@ss25.0202
555	@dear__mybabies 

556	@daya_daya_a
557	@zeezeroxxi
558	@morning_0106
559	@s__bombom
560	@luv.__.siha

561	@dohyeonee_love
562	@minjis2s2
563	@ddovely_614
564	@yunseolgongju
565	@ga_eun_520

566	@ckdid
567	@luvuzoo
568	@ttoyulbaby
569	@seol__10 
570	@haedungi_twins


571	@baby_ahggo
572	@helllo_strongbaby
573	
574	@hajun0916
575	@rayul.raon

576	@cuty_eunja
577	강퇴, 차단공지확인필수
578	@_tae_oh_0803 
579	@l.e.e.b.o.m 
580	@3__meow


581	@norang_zip
582	
583	@angel.hayoon
584	@seoineoi
585	@__chae._.seo_a

586	@yoon.peach
587	@juns_tory1019 
588	@ysbaby_taeyeon
589	@ggy_uum
590	@ttogihouse_ 


591	
592 @dub.n.dub
593 @seoyul_221221
594 @_bokdeong_
595 @woozu_24

596 @supersimple_mommy
597 @1420_aon
598 @baekho_krrrr
599 @h._.ee.s 
600 @kim.do_cute


601 @haar_to_seoha
602 @_kwondoyi
603 @seo_woo.dongri
604 @hoddak._.sj
605 @kimchaemin2015

606 @love_mumu2025
607 
608 @gyul_vly
609 @5geumju
610 @ssaltteoki


611 @anvely._.22
612 @from.day.one
613 @ssozi.home
614 @_joowonii
615 @100cat_rihan

616 
617 @jjjoan0728
618 @with_u_junsol
619 @rrro_yuaniii
620 @jjeung_daily


621 @hey_yuliverse
622 
623 @zyzhshkk
624 @doyuliii
625 @pengin_30

626 @jjeong_ww
627 @wooha_kbnl8853
628 @lovely_hachae
629 
630 @yomyom_soyul


631 @bebe.chaei_sia
632 @venus161230
633 @siooony_
634 @duyul.home
635 @minakkokko

636 @sl_momville
637 @sh._.sy_luv
638 @little_woo_m
639 @_roa__daaa
640 @h_jjun.lll


641 @hi._.bbuu
642 @yena._.ak
643 @luv___bami
644 @yaongsister
645 @yena_ttiyong

646 @han._.janggun
647 @harin_withmom
648 @twinbebe2025
649 @k_94yoonji
650 @gold.kidy


651 @zzio______
652 @bbang_ddojun
653 @hyeoki_mama
654 @eunchae_toto
655 @rintwins.2024

656 @juhyuk_home
657 @heeee_93
658 @s__eun_g
659 
660	@my.son.kim


661	@yumyum___2
662	@yong_yong__mom
663	@_jaeminjaemin
664	@dtdcz
665	@oct._.geomi

666	@ssun_hk
667	@wxxchxitrip
668	@e.joon.e
669	@bebe_suhyeon
670	@moon_minjoon_


671	@coco_elui
672	@seososister
673	@bbo._.bbob
674	
675	@e.hoya

676	@dh.sh.love
677	@lee.seo_love
678	@zoom.in_bomin
679	@harin._.0
680	@han_beeee


681	@yee__jeen
682	@dduddu.min
683	@hi__dongdong
684	@z9.min
685	

686	@dh__paul_
687	@jumin_center
688	@raminnii_ 
689	
690	


691	@jae_a_is_love
692	@soundkim_5
693	@hiyul_iii
694	@_brave_24
695	

696	@taeha_house
697	@ha_binnnnn
698	@bokdung_2yam
699	@luv_taeyoon_1112
700	@hoababy2024 


701	@lovely_taerin1231
702	@glad.you_
703	@hhe_wn
704	@hanarin._.twins
705	@dbwls914

706	@seohan_bombomee
707	@p.j.soo91
708	@baobei.wanan
709	@im_jiny
710	@luv__2a


711	
712	@on_air_jiwoo
713	@jian_ggongju
714	@vltbd
715	@my_angel_2s

716	@chaer__home
717	@yangara2874
718	
719	@yulpooh
720	@cong_al_e


721	@hye_woo_on
722	@nakyoungig
723	@merry._.yun
724	@aminlove1004
725	@merry_mom__

726	@youjin.kim
727	
728	@hello._.jyoon
729	@ro._.rovely
730	@rara_k_land


731	@ham._.bagi
732	@myboy_.junie
733	@_popo.zip
734	@ddumom.daily
735	@ke_vin.zip

736	
737	@ttangttang_
738	@kyeom.d
739	@chacha_ahri
740	@hello_dinoya


741	@genieinjune
742	@2na._.eun1
743	@chae_ha20
744	@zzzisoo__k
745	

746	@chaeeun._.23
747	
748	@lovely__bb.d
749	@baby_jouju
750	@jini.n_mini


751	@zeha.zoah
752	@bbeom_s20
753	@ho._.0luv
754	@ddajeong
755	@home_joody

756	@iam_juhee1004
757	@04ra_daaa
758	
759	@2_dami_2
760	@seo_onnny


761	@hayan_con
762	@the_teo24
763	
764	
765	@hi_bbangs

766	@zzo_mi_
767	@seul.__.bom
768	@two._.seon
769	@_topher_lee
770	@2023kimsan


771	@alllcong
772	@bokddeong_siha
773	@yeayea_2019
774	@2do_luv
775	@kuang_mir

776	@o_tjdwl_o
777	차단공지
778	@remonii23
779	@hangbbok11
780	@yulkong_1120


781	@wonye._b
782	@yongyong_gram
783	@isu_tory
784	
785	@rubyyami

786	@mychan_1220
787	@jua_hwang24
788	@yj_dohyun
789	@seo.woo_ne
790	@bok_dung__2


791	@seowo_o_s2
792	@mylove_peekaboo
793	@06_05.jjw
794	@hi__a.rin
795	@coo.kie_moon

796	
797	@love_pseula
798	@clara._.jiny
799	@sw__0501
800	@mariposa_2148


801	@dam2sol2
802	@luv_woong_happy
803	@dmswn_momo
804	@lavely.1016
805	@loveji_yu

806	@woodoong_twins
807	@yippee_tt
808	@i.am__shalom
809	@yi._.jinn
810	@rambogeomghini24


811	@nair_uyir
812	@92.05_been
813	@taeri_111
814	@soldeun_twins
815	@y__woovely

816	@havelyz_is_myboo
817	@lalammomm
818	@09_twins_05
819	@luro__twins
820	@kongijae


821	@dnsl90
822	@_240115_
823	@goodboy_do
824	@kjjs2013
825	@zhaexxi

826	@min_yoon._.baby
827	@lucys__nest
828	
829	@phyeon_h
830	@hooya__jo


831	@bebe.__.woojin
832	@aazinlee
833	@mippeum_ian
834	@bokgenyimom_
835	@kkuuu.li

836	@luv.ji_yul
837	@jelly_my_luna
838	@suahaha11
839	@luhaya__
840	


841	@heeha__vely
842	@ahreumo
843	@pori_immom
844	@jiwook._.2
845	@sihoho1025

846	@choi_yis2o
847	@harinnn_n
848	@eeshaan.j
849	@yoona_february
850	@liv_cham2


851	@lovely_sj_swt
852	@pupi_pupi_1111
853	@u_zoooovly
854	@hi_teunis2
855	@leekeepshine

856	@asiyun0106
857	@luv_littlebean
858	@bit171025
859	@joybro__
860	@chapcong_twin


861	@bonjour_hayul
862	@luv_sh2087
863	@dohyun.yura
864	@ato__seah
865	@0208___0_0

866	@joyfully.da
867	@uha_vvely
868	@myssongha
869	@yullee_bogo
870	@tia171202


871	@newlove_home
872	@luvwoooon
873	@chaeri_day
874	@with_tongtong
875	@gom.doong

876	@no.1__handsome__cj
877	
878	
879	@hyunni0411
880	@___helloha.___


881	@taeri_sesang
882	@song_seo_a
883	@letsgo_luka 
884	@ksw200501
885	@yunahs_diary

886	@j.sso__i
887	@whsm._.mini
888	@juwon._.days
889	@irene0415
890	@sisters_seyoon


891	@baby_ssack
892	@luv.jeyul
893	@hello.jeong
894	@_____seo.ah
895	@chapssali_baby

896	@bokken_ee
897	@haeun_220225
898	@always_sweethome
899	
900	@my_y.w


901	@grace._.praise 
902	@na_star__
903	@blessing_uni
904	@bandi_ya_
905	@lalabebe.7

906	@10ra_on27
907	@twinkkle._.25
908	@kkam_ye_
909	@eunchaejo
910	


911	@kareum_pink77
912	@koeunseul
913	@uchanoon
914	
915	@yepunoo.s2

916	
917	@lovelee_iiiina
918	@ange_byul
919	@nayoung7179
920	@dal.dal_0807


921	@yumjjang62
922	@_jd_home
923	@k____mj1819
924	@uuneee_
925	@_song.jy

926	@rrang.2
927	@rln_____
928	@cha.iyu_
929	@ah_yooni
930	@_ri._.won_


931	@yulstar0212
932	@potatokkukku
933	@haerang_0
934	@rlo_jj_trip
935	@yejun190715

936	@yuani0410
937	@__hani_mom
938	@love.h.rang
939	@haeyoon_c
940	


941	@jbeom_pk
942	@acorn_song
943	@s2._.zip 
944	@my_lovely_ha
945	@luv.s_woo

946	@suengsuen
947	@lovely_babyduck_
948	@jjo_rang_ee
949	@yunane.zip
950	@eden._.daily


951	@jh_jjihn.k
952	@r.kong.home
953	@haeun_luv16
954	@oi_b_r_o
955	@soso.__.mm

956	@jsbbmwoo
957	@you._.juuu
958	@woni.bomi_ 
959	@hjkim694645
960	@_ddo._.rong_


961	@gion_dayu__
962	@q.hannah__
963	@saeah.nm
964	@lotto_emi
965	@luv__dduck

966	@triplets_sss2
967	@tickled___pink_
968	@sunny._.suh.jin
969	@_so.vely_
970	@_dear1ucky


971	@_all.my.days
972	@won2_only 
973	@with.dybaby
974	@rang.1127
975	@my.moo0e

976	@my._.noel
977	@mom_dalrabbit
978	@siwoo_0o 
979	@som_ang__
980	@ayoon._.i


981	@kimminjung___
982	@shin.wooju.zip
983	@mm.minha
984	@k.ddobok
985	@pudding_o_o_

986	@ggyul_loveday
987	@song_onha
988	@100s2_jh
989	@hwang_family._.0607
990	@my._.bbo_ki


991	@2020_1119
992	@seoyulluv
993	@ji_ho_.1
994	@ss_bebe_
995	@mong3ha

996	@mootal_e
997	@noah_log
998	@hwani__park
999	@my_joyful_12
1000	@babyna_play


1001	@uno.zip_
1002	
1003	@lovely25osh
1004	@with_jjaejjae2
1005	@anbrother_

1006	@o3o_2se 
1007	
1008	@_1dong_
1009	@shimi_gram
1010	@joo_yeon649


1011	@j_minseo
1012	@hi_haone2018
1013	@jeongpan_1206
1014	@suho._.ne_
1015	@haru._.papa

1016	@b_p.zip
1017	@a.j_ch1028 
1018	@_lee__sy
1019	@my_bohol
1020	@choily_zip


1021	@eu._.nwooo
1022	@___som2tae
1023	@yeojun_0918
1024	@awesome_yujun
1025	@25_suho_angel

1026	@p.yunho512
1027	@with.seoro_
1028	@oomun_s
1029	@h.j_leeee
1030	@mppp_home


1031	@march__sy
1032	@_vomvely
1033	@t._.zzoon
1034	@cold_.chan
1035	@jj._.un_5

1036	@doni_world_
1037	@a._.yun_ss
1038	@e.roun_
1039	@jsh_250215
1040	@chaei0215


1041	@bo_bodam
1042	@licba90
1043	@triplets_aaa_
1044	@_idoong_
1045	@nahee__daily

1046	@cecece_3_dgs
1047	@rihan.kim_
1048	@cchae_mama 
1049	@miu.yiru
1050	@geumbok__mom


1051	@sian._.1003
1052	@jiyu_yeyo
1053	@__kong.days
1054	@100.homema
1055	@bbozzabbo

1056	@mei.home__
1057	@dream.comming
1058	@oh_mong2
1059	@little.pudding_luna
1060	@ppukku.ne


1061	@papa_yoooon
1062	@hi.yuriel
1063	@_yunkko
1064	@hapbbbbi
1065	@lim__si_woo_ 

1066	@doo_o_a
1067	@ol_chaea
1068	@kkul_doi
1069	@da.onii_
1070	@ddunddun_jo24


1071	@solhanbly__
1072	@ha.jun_ee
1073	@jjaeyee
1074	@__ha_e__
1075	@_s.seoyul

1076	@welcome.dohaland
1077	@h._.sunny
1078	@kwon.doah
1079	@_.ye0ng._.j
1080	@onong59_siwoo


1081	@haennie_day
1082	@a__jun0404
1083	@candy.25.11
1084	@chae._ah_
1085	@hello.yunwoo

1086	@chaerynlim
1087	@siu__say
1088	@babybada2025
1089	@dodaonyu_u
1090	@ttobok2.s2 


1091	@woori_choib
1092	@happie_daon
1093	@un.nnuu
1094	@with.hoo.and.a
1095   @hyblossoms
1096   @_na_na_zzan
1097   @dowonie_e
1098   @shu.n.rya
1099   @the.hyunniverse
1100   @maplebabe


1101   @baby_dodo.25
1102   @sae._.bome
1103   @kjh_kimjihi
1104   @by._jun
1105   @choi._yul

1106   @bangsso21
1107   @jun_250307
1108   @growing.woojoo
1109   @yoon_a_mom__
1110   @heerang_mom

1111	@gong_na_ye
1112	@im.mumuu_
1113	@loverreumi
1114	@hae_yuni
1115	@fairy.haruru

1116	@ye.seo_mom
1117	@doahyun_0221
1118	@seaweed_leah
1119	@haalanping
1120	@ppigrabbit_8


1121	@jooyoung5959
1122	@bluedays.tx
1123	@jieuni503
1124	@siwoo_love1005
1125	@luckymom0203

1126	@bomian_ing
1127	@ddoyul_vely
1128	@minjaedayday
1129	@monosally17
1130	@kimu_dohee


1131	@danwoo.__.2
1132	@kim.dalcom
1133	@ohmy_gosh2024
1134	@d.do_0s2 
1135	@lim__e.w3

1136	@sia24_s2
1137	@ju_arim.zz
1138	@sihobebe
1139	@chu_bbog_e
1140	@hdh_jinjin2
"""  # 생략된 부분에 전체 데이터를 그대로 넣어야 함

# 라인별로 분할하고 @로 시작하는 것만 추출
usernames = []
for line in raw_text.strip().splitlines():
    parts = line.strip().split("\t")
    if len(parts) >= 2:
        username = parts[1].strip()
        if username.startswith("@"):
            usernames.append(username)

# JSON 파일로 저장
with open("instagram_usernames.json", "w", encoding="utf-8") as f:
    json.dump(usernames, f, ensure_ascii=False, indent=2)

print(f"{len(usernames)}개의 유효한 인스타그램 ID가 저장되었습니다.")