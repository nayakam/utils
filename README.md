GoogleMapAPI_DR_BOT
AIzaSyB_nfdLf7APO8_gYwmjQdv5jubDELqAdw0

https://maps.googleapis.com/maps/api/directions/json?origin={PARAM_ORIGIN}&destination={PARAM_DESTINATION}
&key=YOUR_API_KEY

https://maps.googleapis.com/maps/api/directions/json?origin=Wollongong&destination=Adelaide&key=AIzaSyB_nfdLf7APO8_gYwmjQdv5jubDELqAdw0

pip install -U googlemaps
pip install ujson

https://googlemaps.github.io/google-maps-services-python/docs/
Travel Modes:
https://developers.google.com/maps/documentation/directions/intro#TravelModes

##### API Request Result format

Get distance result for address

{
   "destination_addresses": [
      "Wollongong NSW 2500, Australia"
   ],
   "origin_addresses": [
      "483 George St, Sydney NSW 2017, Australia"
   ],
   "rows": [
      {
         "elements": [
            {
               "distance": {
                  "text": "85.0 km",
                  "value": 84991
               },
               "duration": {
                  "text": "1 hour 46 mins",
                  "value": 6376
               },
               "status": "OK"
            }
         ]
      }
   ],
   "status": "OK"
}

###### Get directions result for address
```json
[
   {
      "bounds": {
         "northeast": {
            "lat": -33.873592,
            "lng": 151.20837
         },
         "southwest": {
            "lat": -34.4278,
            "lng": 150.88824
         }
      },
      "copyrights": "Map data ©2017 Google",
      "legs": [
         {
            "arrival_time": {
               "text": "12:17pm",
               "time_zone": "Australia/Sydney",
               "value": 1500776242
            },
            "departure_time": {
               "text": "10:24am",
               "time_zone": "Australia/Sydney",
               "value": 1500769458
            },
            "distance": {
               "text": "85.0 km",
               "value": 84991
            },
            "duration": {
               "text": "1 hour 53 mins",
               "value": 6784
            },
            "end_address": "Wollongong NSW 2500, Australia",
            "end_location": {
               "lat": -34.4278,
               "lng": 150.89288
            },
            "start_address": "483 George St, Sydney NSW 2017, Australia",
            "start_location": {
               "lat": -33.873592,
               "lng": 151.207
            },
            "steps": [
               {
                  "distance": {
                     "text": "84.3 km",
                     "value": 84348
                  },
                  "duration": {
                     "text": "1 hour 45 mins",
                     "value": 6312
                  },
                  "end_location": {
                     "lat": -34.42695,
                     "lng": 150.88828
                  },
                  "html_instructions": "Train towards Kiama",
                  "polyline": {
                     "points": "||vmEwr{y[A^hAHnAJ@?@?hDh@h@HXFfARp@Ld@DF@H@nAK|CYzB[nDq@pBo@~Aw@@?HGlB{ANO`@Ub@Yp@c@p@Wp@MbA@|ATzA\\`A^h@XJF|Ad@r@Xl@TzD`CzE~D`D|DdCpDtCrErBbElAtBn@hAjBrBt@l@r@f@t@h@nClARFy@jAFFLRNVP^LThArCRf@DNXx@FLn@bBL`@N`@d@hA`@fAPh@L^HZLb@Lf@Lh@Pv@Jh@H`@Jh@ZxAH\\ZxA^zAl@hCn@tCJ^Nn@Pn@Xz@Rl@N^Rd@P\\R`@P\\HJXh@\\n@`@n@R\\RV^d@^b@^`@VTHHbAt@v@d@x@b@p@\\d@T\\HXJVJ@?b@JJBFBPFj@NZFD@`AP|@PhAPlB\\hB`@B?B@D@F@ZDt@LvAPl@J^FPFLBh@Lb@LPFjAd@p@\\ZVHFFBj@b@v@z@n@r@j@t@`@n@f@x@`@x@P^HRv@dBPd@N`@Rr@BLJ\\D\\Hb@Jx@PpBLtADZHl@d@jCd@pCLj@P|@H^XjAd@xAHXL\\^`Aj@rAJVLVRb@P^h@bA|@`BrAzBhAnBnB`Dl@fAt@nAz@zAdBvCnBjDRZ\\f@d@l@r@|@d@h@p@x@Xb@d@v@z@tBZr@d@`AXh@Td@`@r@n@rAv@rA|@|ATf@Tb@hCtEp@nAlA~BpC|EdA`B`AnA~@bAxArAz@p@rBdAbBn@ZLXHRD\\FnC^TBfAJpAL\\DNBh@Jv@RdA^jDnBDBr@f@z@j@bAt@bAv@dA|@nAlA\\\\\\^t@v@jAjAHLjBzBzBlCzAjBPNFFPPvAxAj@n@f@h@RRh@f@B@^X\\Tz@b@f@RdBr@h@RLFd@P@?RHlItC`@PjATfBp@FB|@d@bB|@hBx@lCjAZL^THDJFTL?@^XPN`CpB~@|@z@`A~ArBpAfBv@`An@v@d@l@VZZ^f@b@d@`@d@^^Vz@h@h@Vj@\\XNZL`@Jp@ThAf@XLv@ZXNLBj@XXNh@XTJRHp@Z`@Pb@RTHb@RB@\\Ll@Xj@Vl@Vj@Tl@Xz@^x@\\|@^j@Vf@Th@Tf@T^L^Lx@VbAZh@NTHj@Pv@^K^hAh@@?^P`Aj@x@^dCbApEhBlAf@nFjB`G~AfEfAtBl@f@LbDp@rB^|Bd@@@v@N|Cn@@MjAX~Bj@x@Tj@R`A\\~@b@xAbAfAdAp@n@b@h@b@n@Zf@^j@Vh@f@jAp@hBHRDRBLDNNr@XxAD\\r@fFf@fEr@fEJl@l@tGXrCh@bFf@rEl@dFj@~EHv@@P@PBTHz@DrABz@ApAAp@El@Iz@MhAE\\XFADKn@Ox@Kh@Ql@Qn@K`@Qr@Mf@Qn@Of@Mh@Mf@I^G\\Kd@Ml@E`@If@Ef@Ef@Eh@El@Ch@?d@An@?h@?d@@T?VBtA?V@XBv@Bx@Bh@BlA@lAAt@GpAO|AQdASbAG\\Mj@]vAeAhCQd@yApDm@dAaAbB[n@aA|B[r@a@vAUv@SbA?@O~@Kz@K`ACl@AVCXCn@At@?`A@fABz@FlAF~@Fx@H~AFt@Bf@N`CJbBZlERrCJ`AF`@h@fG@JTpCHz@Fj@Fl@TrAHd@Ld@Nj@Nj@Tl@HXHTHT@B\\z@N\\Zv@NXJTNZv@rArAlBp@~@h@l@pAzAp@p@`Av@bAl@HF@@LF|@h@nAt@B@h@Xh@Td@Rv@VdA^r@Tf@Pd@J|Bh@h@`@bAj@nB|A|A~@f@Vl@Xj@R@@LB`@H`@F\\Dd@Bd@Bb@?\\?`@C`@C^Gb@IZG~Bk@l@GfBWn@KZEHA`@EPCNCD?LAt@EF?|@Cf@Bn@Fh@D\\FZFVFbA^hAn@dBjAlBpA`Ap@z@`@r@^l@Rb@JVFZDf@F^Br@@p@?vCEv@?t@Bn@Df@Ft@Pb@LXLXL`@Tp@`@rB|AfClBpBzAdCxBlB`BdD~CjBdBz@v@rBpBjAlArC|CfEvEzDlE\\^\\Zb@^dBxAv@b@h@Xv@Zr@R`AT`ANp@Hb@Db@BhAAp@Gr@In@Gn@K`@K`@M\\MVM^Qz@g@x@m@\\Wb@_@`@Y`@Yl@_@d@UZO\\O\\Od@O`@Mt@OZI`@Gd@C^CL?X?R?\\@^BVBPB\\HZHd@LVJ`@T^T^Zf@b@\\\\X\\`@f@~@jAhBvBd@h@^`@^^h@d@^\\`@\\`@Vh@Zd@Vr@Z~@\\l@Td@L\\H\\FpCTv@Dl@?v@A`@CVAfDWrAMz@Gr@GDArDYb@Cn@CJAlAC`@?bB?bABbADf@BdAJ`BPbBVbB^hCr@lAd@bAb@dCpAbC~A|@l@p@b@pAz@~@l@lAv@pAz@tBtAhAt@JFx@h@vA`ArAz@`BfArBtAB@jAt@FD`Al@\\R~@r@bCzAn@`@l@b@NLxBvA~AdA|B|An@`@h@Xn@b@v@f@t@f@l@b@|@h@h@^nAv@~@n@x@h@j@\\XNZPr@\\h@Z`@ZjAr@`Ap@v@f@n@Zz@`@n@Zz@Zl@Rd@Jl@Nl@Nt@Nr@Lv@JlAJp@Dv@B|@Bd@A|AAl@AvACd@CvEk@|AQrBUrAK`AC~@@n@@^@XB\\BVBZBZDRDXDZFb@Jd@L`@L\\J`@N^N`@RXNXLRLNHTNZRZT^X\\ZXVPPZZVXTVRTPVV^PVJPV^d@z@@B`@|@Vp@b@|ALh@@@tA~E`BxFdAnDdCnIrAvEr@fC~@`D|B~HhDtL`DdLzA`FpCtJDLbErNbAhDhA~Dp@`C`AfDjBxGRj@XbAZbAv@fCb@xARr@Nf@@DJVRn@Pb@L^P`@\\z@Zt@Rb@Xn@`@x@b@r@Zj@l@fAfAdBJLb@p@l@|@n@z@DDl@r@b@f@VV|@~@~@z@bAz@l@d@@@HHDBrAbAt@h@\\TtA|@vAx@xAr@XLr@ZZLr@XpAb@pA`@rA\\lAXp@N\\FpARpARN@`AJz@F|@Fl@BjAD|@BfABhA?hA?nACL?~A?pDEhA?bB@J?jBAjBCbBCpA?jBCpA@hAFjALjANJBTBRBNBt@Nz@Rd@Rn@Vh@Tl@Xj@Xh@^`@Vj@b@XTZVVXPPTTRTn@r@l@p@d@f@`@b@l@n@DFf@f@j@n@^^r@t@\\^h@j@h@n@f@h@TTVXb@b@bAfAt@z@fAjAx@|@j@p@t@t@v@z@r@v@z@~@r@v@~@fAv@z@b@f@x@x@fAjA~@bAv@z@t@v@t@x@tAzAhAnAtAvAt@x@p@r@r@t@t@t@t@r@r@n@v@n@t@h@p@f@z@j@`@Vn@`@h@Xf@Xn@\\p@XhAh@fAb@x@XtAb@`AZr@P~@Td@J|@Pn@HfAPvALzAPnAHx@D|@DtBFpCFdBDtBHnCFpBF~BJ~AFfBDdAD~AD`BD~ADfBDzBFhBFxBLdBDpAFj@@N?`@?^@|ABpBDvADrBFv@BxBD~ABbB?jB@pB?rBAt@AfAA`AA\\C^?fAEzAIlBGH@L?NBHA`@Cp@EVEt@GvDWjBKnAIxAKhAGjAInAIfAGxAIdAG`BK~AMzBOx@EjAI~@Cj@Ad@?z@@b@AVAl@GDA~@Or@KTCn@Af@GrAI`AGl@GREFADAB?DAD?FAD?B?HCV?Z@f@@z@Jp@H^FdAPZHZFZDXB`@@`@@Z?RAd@Cb@EbAOb@Ib@OLGn@[n@]z@i@`@Sx@a@`@Ov@Qh@K`@G`@Cf@Cd@?p@Bn@D|AJt@FfAJrAHhAJrALbAH`AF~@FdAHhBNnBJnAJ~@Hx@FvALtBPpAFn@@n@?XAh@Gd@Mb@Qd@S`@YVWb@i@b@o@v@}Ab@{@n@}@b@e@b@W`@Qf@S|@Oj@Av@F~@NPDTLb@V`@\\\\ZZd@nAbCh@dAT\\VX\\\\d@Xd@Tt@TzAd@p@Tt@\\TN`@^d@h@T\\Xh@Rd@J^Tn@Pp@JXZ~@x@zB^fAVt@\\`A^fAh@`BPh@^dAFPHRLVZf@NTNPPTPLTN^Tz@\\nAPlAB|AUnAc@bBuAr@mAh@{AXuAJeAC}AImAc@cCGMu@uAiBmBsAqAa@c@s@cAUi@e@uAm@_Bm@oAc@y@c@m@w@{@]a@[YY]Y_@Y_@Oa@Wo@Me@Ii@Ga@C[Ci@Ae@?g@B_@Bc@D_@F[H[J[Tw@DMTc@HQT]f@o@XWj@i@b@_@d@c@p@m@dByAfA_AnAcAXS\\OVKf@MVEZEb@AtADf@F^HXJVJZPXPj@d@X\\b@r@R\\Xr@^vATtAZnBRx@Nf@\\v@`@j@LPXXPPXTXNl@Xp@P~Af@xAb@XHPLj@Xx@n@VTX\\\\b@v@lA\\r@Pb@Rp@`@nAJ\\Tz@\\~@FVPl@\\jAjAdDZl@Rd@RZTVRRNLZRVPXLb@J`@Fl@Db@?^E\\Gt@SNITI\\W\\[\\c@Xg@Vu@Pu@JeA?u@As@AMMcBKe@]aAc@{@g@o@c@g@_@c@_@i@a@i@]s@Wm@IYIYGYCQcAuCg@gA[c@]a@cA}@}@y@y@q@qAuAc@y@Ww@UeAAUAoADaAJo@TsAPm@t@iBp@cAf@u@r@mAjBsDDIhBsC~AcCpAaBtBuC`AcA~@s@RI`@EJ?LAZ?V?VBr@Fx@Tj@R~@d@r@b@z@f@fAd@dBNR@jAD`AF|@Fp@DF@l@Vz@f@bAx@z@pATb@Rd@h@rA`AxBd@tA^rAPhAv@dGFTJRFFHNLJJLXVLLLJj@Z^TZZt@v@Xf@DFBDj@Dj@?`AGt@Sp@]vBwAFGDELKRSTU`@_@hIwJV]^i@V_@RYVm@Na@Le@Nm@J_AJ{BBm@HkAJs@DQPc@N[L[X_@^c@RSTM\\QXMf@Mb@Gr@EZ?`@A`@@h@Bj@Bh@@T@h@Bx@Db@@|@DVB\\Bt@FRBVD^Hd@Lf@Nf@TLDVLZN|C|Br@^j@\\n@Zp@Xt@Pt@LdAFx@Bv@?|@IzASxAi@pAq@dAo@`H{DhAm@ZQd@W\\Ol@M`@El@Ab@Af@BTDh@PRHNHTLb@X`@f@d@|@h@rAb@~@`@h@p@r@j@`@~@\\fARb@Bl@Br@Ef@Gj@Ih@@r@Fh@Hb@R`@TXTPRZf@HNPZVp@HZHj@Fd@@p@?p@GhBIvACj@Cz@?v@Fz@Dd@FZH^Ph@`@bALXXj@Xl@Vl@h@nA\\v@\\t@n@jAZl@Xj@P`@Tb@\\p@P^NZb@z@Vj@\\n@l@x@TTPLZT\\T`@RTHXHTFb@FTB`@Bf@@d@B|@BVBxAR\\Jb@PZNPLb@`@^^LNPVNVLZFLHVRd@Xt@Nb@Tl@Xt@FRTb@R`@\\l@RZ^^RRNLPNLLbBfA|@h@t@b@b@Tj@XlAl@`BfAp@t@d@h@LPLRZn@Lb@HZJj@Hb@D\\Fd@BZBZ@f@Bj@@b@@V@^?b@A\\GbAAVCh@Cr@IhAAx@A|@ChAB|EDp@Jt@Hl@H`@HVR\\Vh@R^NTTXNNTRXNZP\\PZJ`@Lh@DpCLL?hA@z@FH@ZFTFXJPF\\RTLRNNLJHHJn@v@\\t@Vn@^z@\\dAZjA^fBVrAJt@Dz@Bz@@bA?jCRtA`@~A`@hARd@LTV\\\\XJJLJZRb@PZHd@HXDXBb@BV?VA\\Cd@GZIZK`@Q`@Sd@[\\WROFQBIDMJk@JgAL_CJwDFcC@oC@kAt@qIDs@BmA?w@CmBAi@Ao@?u@@cA@]DWFk@F_@J_@J]Pc@Vg@NSV]n@o@JIPMTMRIRKb@MNELANCNAZCN?R?V@TBRBRDXFRFXJTHNJPJVRPNPPTXNPJRx@vAh@~@n@dAh@x@`@h@h@p@`@d@f@h@f@l@RXTTfBlBnBxBfBtBbAfA~@jAh@r@j@bAd@dAj@rA?@ZQZv@Tx@RxAfA~Fn@vDlBtKp@hDl@~CLl@T~@Nh@N`@JRNVHLJN\\^RNTTj@Zl@T`@Nj@LZ@dA?`@ApBKvD]~Fu@|@UrF_BpTgGtEiB^IVEr@GJ?N?ZBL@h@Ld@LNHd@Rb@ZVTX^V\\T^Xf@~@zAj@dAt@`AzAtAx@z@RH\\Rb@ZfAn@nBrAxAbAl@\\x@b@nAb@l@PvA\\lBXdANj@DnALlATv@Xf@T\\NVNn@h@XVf@j@\\Zd@j@T\\\\h@`@n@nAnBfA`B|@rAv@pAdA~AjAfBp@dAr@hAn@`Ad@x@Xh@Th@Rn@JXLb@HZHd@F^DXD^HdAJdADn@D\\Jj@Lr@H^Pl@JZN^Rd@R\\Xb@T^PRPRVVPPTPj@^RJRJRHXHTHZFfAPz@@fA@L@b@?\\@ZBJ@VBXF\\HXH`@NPJVNB@RNVTNLPRVZPTRZT`@lApBVZTTRTZTZP^RVJ`@NVFRDb@FXB`@@^@^Cv@EnAMdD[n@Gp@Cd@?f@@XBTD^HJ@VH@?THZLTNb@Vd@`@d@d@JNTZ\\j@^|@Nf@Pr@F`@DZLtAJdAFr@Dd@RbABNJ`@HRP`@N\\NTNTPRTXXXPNXR`@VZP\\P^R|CxAjCpAdAd@hAj@dAh@x@\\p@Xn@Tx@ZZNd@Rl@X@@@@PHZRlAz@z@l@|C`CHFDDHFVRlBxARNTNVP^Ph@Zd@RXLd@NLDf@NPDhAXl@LhCd@ZFXD~@LdDf@hDf@lARj@LXHPFl@V\\N`@XZTRR\\^nA`BlBdC`CbDhDtEx@dAlClDx@fApBlC`ApAbAtA@@BBPXjHtJfB|BbAtAr@`A`@f@t@dAn@z@TXrD~EPRLLVXd@d@p@p@VVZZ~@z@`Az@ZX\\Vf@\\`@Z`HdFbFtDvCtBhBpA|@n@z@n@dBpAx@l@ZTr@f@l@b@PLFFdAr@FF`@Xh@`@h@^l@b@PLp@f@`@Zz@n@^Xb@X`@XZV`@XTNLJ@@HFdBrA~@l@TPTPbAt@p@d@`Ap@r@ZZLVFTFz@Lr@DV?Z?n@Eh@Gb@Ib@Il@OhA[t@OlAY|@S~Bi@|@Sx@Qt@OhAMb@Eh@AT?b@A~@@r@Dj@Db@Ft@Jj@L|@Vj@NnA^XHjA\\JDLDbAXVFj@P^JZHnF|AlAZfBh@PFVHlBh@t@TnA^b@JnBl@^J^Jj@Nh@Lt@Pd@Dj@Dd@B`@@n@?X?n@Cd@Ch@Ij@IPGl@Ql@S`@Qv@a@XQRMzAkAbCsBZW|@u@|@u@h@a@VSPKNI^S\\ONGb@O`@Kr@MHAl@GJAv@E|@@n@DVBJ@TBd@JrBl@pDbAvDbALDLDjA^`D|@NDxBl@nBh@|EzAfGbBlGhB`FxAfD`AlBf@xBn@hCv@~@VrA^vCz@r@TjBf@|Br@xA`@nAZp@LnATVFlAX^Jv@VlAb@j@VbA^n@TbAZvErAjCv@^LbD`AnBh@vBj@f@Nr@TvBl@zC|@nBh@vBn@dFxA|Ab@rA`@d@LJBjEnAfBh@x@TvDhAtEpA|GnBB@xC~@dDdA`@LlA^pBp@|Ah@nAb@~@\\fA\\v@XDBv@Xn@Tp@Tx@Xp@Vp@TpAd@vAd@fBn@|Aj@bA\\bBl@tBt@tBr@z@ZbA\\bA^|@Z`A\\hA`@zAh@`A\\p@TbBl@fBn@jBp@tBv@lA`@j@P`DhAf@PfC|@rBr@nBr@xAf@tAd@dBl@p@Tl@Rz@TdAX|@RbARp@LhAP`BTlBTvC^~Cb@zBXnBVlC\\pBVlBXpC\\fC^lC\\bBRbBRbBTd@FjAPtAPB?dBTbCZnBVrARvAPxARlBVlBTzARrBX~En@TBb@Fx@J^F`ALl@Hl@Hp@Hh@Hv@ND?RDh@HbALjANXDNBPBZD`ALhANpAPdANVBt@J`ANt@Hv@JLBx@JrAP|@LdALx@LB?@G"
                  },
                  "start_location": {
                     "lat": -33.873592,
                     "lng": 151.207
                  },
                  "transit_details": {
                     "arrival_stop": {
                        "location": {
                           "lat": -34.42695,
                           "lng": 150.88828
                        },
                        "name": "Wollongong Station"
                     },
                     "arrival_time": {
                        "text": "12:09pm",
                        "time_zone": "Australia/Sydney",
                        "value": 1500775770
                     },
                     "departure_stop": {
                        "location": {
                           "lat": -33.873592,
                           "lng": 151.207
                        },
                        "name": "Town Hall"
                     },
                     "departure_time": {
                        "text": "10:24am",
                        "time_zone": "Australia/Sydney",
                        "value": 1500769458
                     },
                     "headsign": "Kiama",
                     "line": {
                        "agencies": [
                           {
                              "name": "NSW TrainLink",
                              "phone": "011 61 13 15 00",
                              "url": "http://www.nswtrainlink.info/"
                           }
                        ],
                        "color": "#0277bd",
                        "name": "South Coast Line",
                        "text_color": "#ffffff",
                        "vehicle": {
                           "icon": "//maps.gstatic.com/mapfiles/transit/iw2/6/rail2.png",
                           "local_icon": "//maps.gstatic.com/mapfiles/transit/iw2/6/au-sydney-rail.png",
                           "name": "Train",
                           "type": "HEAVY_RAIL"
                        }
                     },
                     "num_stops": 17
                  },
                  "travel_mode": "TRANSIT"
               },
               {
                  "distance": {
                     "text": "0.6 km",
                     "value": 643
                  },
                  "duration": {
                     "text": "8 mins",
                     "value": 465
                  },
                  "end_location": {
                     "lat": -34.4278,
                     "lng": 150.89288
                  },
                  "html_instructions": "Walk to Wollongong NSW 2500, Australia",
                  "polyline": {
                     "points": "l_cqEwj}w[@s@A?GCCAAAAAAA?CAA?A?CAC@E?G?I?I?C?E?GACAECKAGIKMMIGCCEECCAC?CAAAKEWEg@AKAQ?IAGAICIGSSq@EUS]M[E{@Ce@A_@Ck@A]Aa@@a@N{BFu@h@H~FZL@ZB"
                  },
                  "start_location": {
                     "lat": -34.42695,
                     "lng": 150.88828
                  },
                  "steps": [
                     {
                        "distance": {
                           "text": "0.1 km",
                           "value": 115
                        },
                        "duration": {
                           "text": "1 min",
                           "value": 89
                        },
                        "end_location": {
                           "lat": -34.426502,
                           "lng": 150.88956
                        },
                        "html_instructions": "Head <b>northeast<\/b> on <b>Station St<\/b> toward <b>Auburn St<\/b>",
                        "polyline": {
                           "points": "l_cqEwj}w[@s@A?GCCAAAAAAA?CAA?A?CAC@E?G?I?I?C?E?GACAECKAGIKMMIGCCEECCAC?CAAAKEW"
                        },
                        "start_location": {
                           "lat": -34.42695,
                           "lng": 150.88828
                        },
                        "travel_mode": "WALKING"
                     },
                     {
                        "distance": {
                           "text": "0.3 km",
                           "value": 338
                        },
                        "duration": {
                           "text": "4 mins",
                           "value": 244
                        },
                        "end_location": {
                           "lat": -34.426098,
                           "lng": 150.8931
                        },
                        "html_instructions": "Continue onto <b>Burelli St<\/b>",
                        "polyline": {
                           "points": "r|bqEwr}w[Eg@AKAQ?IAGAICIGSSq@EUS]M[E{@Ce@A_@Ck@A]Aa@@a@N{BFu@"
                        },
                        "start_location": {
                           "lat": -34.426502,
                           "lng": 150.88956
                        },
                        "travel_mode": "WALKING"
                     },
                     {
                        "distance": {
                           "text": "0.2 km",
                           "value": 190
                        },
                        "duration": {
                           "text": "2 mins",
                           "value": 132
                        },
                        "end_location": {
                           "lat": -34.4278,
                           "lng": 150.89288
                        },
                        "html_instructions": "Turn <b>right<\/b> onto <b>Keira St<\/b><div style=\"font-size:0.9em\">Destination will be on the left<\/div>",
                        "maneuver": "turn-right",
                        "polyline": {
                           "points": "bzbqE{h~w[h@H~FZL@ZB"
                        },
                        "start_location": {
                           "lat": -34.426098,
                           "lng": 150.8931
                        },
                        "travel_mode": "WALKING"
                     }
                  ],
                  "travel_mode": "WALKING"
               }
            ],
            "traffic_speed_entry": [],
            "via_waypoint": []
         }
      ],
      "overview_polyline": {
         "points": "||vmEwr{y[fAh@pAJtEr@zGf@zPwCxE{CfCcBdGMnQvH|J|JzGdK|IvNnHlEe@rATZxB`Fz@~B~D~KxB|JpErRrCxG`FjHlI|EpRbEhG~@xGjCzG~HnD|IvAjL~DfRtWff@lJbNdHzN|P`[`HhInHtDhLzA|K~EjMzKdMxNjH`H|HbDvXpKtGfDhPvQhHpG|PtHtS~I`J`D`AZj@~@jBz@rMxFfWzHjWtFfGlAfGxC|HxKzBzItHfo@zBfUIxKuEbSu@jSHxMaExP{JlUeAbJVrNlBfYxBpTjBvGnDtHbMvMzGnDjNbF`KrFpGL`RoCtIdA`P`JpLT|HbBd\\jXnYvZjFvDnFtAhKS`QoJnGgAnE`@~F`EzJzKzIfEdLd@xRyAtMRrL|BzKzF`RzLp\\pTt^xUpKpGlKhDdNn@jVmBvGZtFvAzK`IzCvEjJb[pm@zuBbMp`@pGhLnHdJvGpFdMbHzObEtM~@pi@O|IdA`J`EbOjOhVxWn]l_@nL|JvKrFxMhDjUvAzt@zBrh@p@bVu@baA_GvHNrGp@fHyAlJsDlL`@pf@jDxCWbCwAbDsFxCmChE]jCz@`H~J|JnEhDrHfGnQlChFbCpA|CTlDy@vCcDbAqDe@uJ{FcHqCgFoHmL_C_HXsG~C}F~LmKtBo@|DDpF|D`EhOnFzDdFbBvC|B|EdLdFfNlE`ChGgAlB}CZeFy@yEoCwDwCuGeDcHmG_GsAmEd@uGpLqThJ_M`CcArHxA|G`C~EVbDfAhDtEpDvJ|AxJlC~BjCpC`BR`HqCn@m@|N}Q~A_NxCsEvG{@zI\\dG`AvKpGbF`AjGY|ToL`DWzBd@jBxAtCzFdFfClDErDHpBrAlBdHKtNrKtV|EtIvEpBrIt@dEpDlCdHfDdFtKpGfExD`AbCp@~GIbH?dSbC~F`FvBzJt@nDtCrEdPJfIjBdHxDtCpFHzEqCdAwUx@_Xp@yHtDsEdDu@fD^bD|BdHxKzMjOfItKjKbj@tBbGjGvCpKk@bf@sL`IaCdADrFhDzJfMjO|IzP|ClF~DfWba@lDpSvCjF`EfClIj@dE`AhJxK~EzApN{@bE`@xErDfC~KlAdG|CtDtPlIjKpEbJtGvF~D`HbCjUrDtFjCll@fw@nWzZtz@dn@`GjEpJtEvHk@xPyDpJIdLpCd]vJlK`C|HUpImE~JcI~F_BpGTleAjZvh@tN`p@zR`}@rWt_@rMfuA~e@~t@pK`m@xHpu@~JpGx@|@LB{@OGEI?o@a@eAu@oDoAwGEmCVqDhHd@h@D"
      },
      "summary": "",
      "warnings": [
         "Walking directions are in beta.    Use caution – This route may be missing sidewalks or pedestrian paths."
      ],
      "waypoint_order": []
   }
]
```

###### Get code result for address

```
[
   {
      "address_components": [
         {
            "long_name": "68",
            "short_name": "68",
            "types": [
               "street_number"
            ]
         },
         {
            "long_name": "Burelli Street",
            "short_name": "Burelli St",
            "types": [
               "route"
            ]
         },
         {
            "long_name": "Wollongong",
            "short_name": "Wollongong",
            "types": [
               "locality",
               "political"
            ]
         },
         {
            "long_name": "Wollongong City Council",
            "short_name": "Wollongong",
            "types": [
               "administrative_area_level_2",
               "political"
            ]
         },
         {
            "long_name": "New South Wales",
            "short_name": "NSW",
            "types": [
               "administrative_area_level_1",
               "political"
            ]
         },
         {
            "long_name": "Australia",
            "short_name": "AU",
            "types": [
               "country",
               "political"
            ]
         },
         {
            "long_name": "2500",
            "short_name": "2500",
            "types": [
               "postal_code"
            ]
         }
      ],
      "formatted_address": "68 Burelli St, Wollongong NSW 2500, Australia",
      "geometry": {
         "location": {
            "lat": -34.426144,
            "lng": 150.89531
         },
         "location_type": "ROOFTOP",
         "viewport": {
            "northeast": {
               "lat": -34.424793,
               "lng": 150.89667
            },
            "southwest": {
               "lat": -34.42749,
               "lng": 150.89397
            }
         }
      },
      "place_id": "ChIJqQm286UZE2sRWqI7IkidVRw",
      "types": [
         "street_address"
      ]
   }
]
```

###### Get address for geo code

```
[
   {
      "address_components": [
         {
            "long_name": "68",
            "short_name": "68",
            "types": [
               "street_number"
            ]
         },
         {
            "long_name": "Burelli Street",
            "short_name": "Burelli St",
            "types": [
               "route"
            ]
         },
         {
            "long_name": "Wollongong",
            "short_name": "Wollongong",
            "types": [
               "locality",
               "political"
            ]
         },
         {
            "long_name": "Wollongong City Council",
            "short_name": "Wollongong",
            "types": [
               "administrative_area_level_2",
               "political"
            ]
         },
         {
            "long_name": "New South Wales",
            "short_name": "NSW",
            "types": [
               "administrative_area_level_1",
               "political"
            ]
         },
         {
            "long_name": "Australia",
            "short_name": "AU",
            "types": [
               "country",
               "political"
            ]
         },
         {
            "long_name": "2500",
            "short_name": "2500",
            "types": [
               "postal_code"
            ]
         }
      ],
      "formatted_address": "68 Burelli St, Wollongong NSW 2500, Australia",
      "geometry": {
         "location": {
            "lat": -34.426144,
            "lng": 150.89531
         },
         "location_type": "ROOFTOP",
         "viewport": {
            "northeast": {
               "lat": -34.424793,
               "lng": 150.89667
            },
            "southwest": {
               "lat": -34.42749,
               "lng": 150.89397
            }
         }
      },
      "place_id": "ChIJqQm286UZE2sRWqI7IkidVRw",
      "types": [
         "street_address"
      ]
   },
   {
      "address_components": [
         {
            "long_name": "Greater Union Cinemas Burelli St",
            "short_name": "Greater Union Cinemas Burelli St",
            "types": [
               "bus_station",
               "establishment",
               "point_of_interest",
               "transit_station"
            ]
         },
         {
            "long_name": "Wollongong",
            "short_name": "Wollongong",
            "types": [
               "locality",
               "political"
            ]
         },
         {
            "long_name": "Wollongong City Council",
            "short_name": "Wollongong",
            "types": [
               "administrative_area_level_2",
               "political"
            ]
         },
         {
            "long_name": "New South Wales",
            "short_name": "NSW",
            "types": [
               "administrative_area_level_1",
               "political"
            ]
         },
         {
            "long_name": "Australia",
            "short_name": "AU",
            "types": [
               "country",
               "political"
            ]
         },
         {
            "long_name": "2500",
            "short_name": "2500",
            "types": [
               "postal_code"
            ]
         }
      ],
      "formatted_address": "Greater Union Cinemas Burelli St, Wollongong NSW 2500, Australia",
      "geometry": {
         "location": {
            "lat": -34.426304,
            "lng": 150.89531
         },
         "location_type": "GEOMETRIC_CENTER",
         "viewport": {
            "northeast": {
               "lat": -34.424957,
               "lng": 150.89665
            },
            "southwest": {
               "lat": -34.427654,
               "lng": 150.89395
            }
         }
      },
      "place_id": "ChIJ6YFp86UZE2sRsDT2l32h88w",
      "types": [
         "bus_station",
         "establishment",
         "point_of_interest",
         "transit_station"
      ]
   },
   {
      "address_components": [
         {
            "long_name": "Wollongong",
            "short_name": "Wollongong",
            "types": [
               "locality",
               "political"
            ]
         },
         {
            "long_name": "Wollongong City Council",
            "short_name": "Wollongong",
            "types": [
               "administrative_area_level_2",
               "political"
            ]
         },
         {
            "long_name": "New South Wales",
            "short_name": "NSW",
            "types": [
               "administrative_area_level_1",
               "political"
            ]
         },
         {
            "long_name": "Australia",
            "short_name": "AU",
            "types": [
               "country",
               "political"
            ]
         },
         {
            "long_name": "2500",
            "short_name": "2500",
            "types": [
               "postal_code"
            ]
         }
      ],
      "formatted_address": "Wollongong NSW 2500, Australia",
      "geometry": {
         "bounds": {
            "northeast": {
               "lat": -34.413548,
               "lng": 150.91104
            },
            "southwest": {
               "lat": -34.442955,
               "lng": 150.87508
            }
         },
         "location": {
            "lat": -34.42781,
            "lng": 150.89307
         },
         "location_type": "APPROXIMATE",
         "viewport": {
            "northeast": {
               "lat": -34.413548,
               "lng": 150.91084
            },
            "southwest": {
               "lat": -34.442955,
               "lng": 150.87508
            }
         }
      },
      "place_id": "ChIJe1YLH6UZE2sRIOcyFmh9AQU",
      "types": [
         "locality",
         "political"
      ]
   },
   {
      "address_components": [
         {
            "long_name": "Wollongong",
            "short_name": "Wollongong",
            "types": [
               "colloquial_area",
               "locality",
               "political"
            ]
         },
         {
            "long_name": "New South Wales",
            "short_name": "NSW",
            "types": [
               "administrative_area_level_1",
               "political"
            ]
         },
         {
            "long_name": "Australia",
            "short_name": "AU",
            "types": [
               "country",
               "political"
            ]
         }
      ],
      "formatted_address": "Wollongong NSW, Australia",
      "geometry": {
         "bounds": {
            "northeast": {
               "lat": -34.25134,
               "lng": 150.97386
            },
            "southwest": {
               "lat": -34.6286,
               "lng": 150.74394
            }
         },
         "location": {
            "lat": -34.42781,
            "lng": 150.89307
         },
         "location_type": "APPROXIMATE",
         "viewport": {
            "northeast": {
               "lat": -34.25134,
               "lng": 150.9738
            },
            "southwest": {
               "lat": -34.628445,
               "lng": 150.74394
            }
         }
      },
      "place_id": "ChIJS8moNtEaE2sRwKgyFmh9AQQ",
      "types": [
         "colloquial_area",
         "locality",
         "political"
      ]
   },
   {
      "address_components": [
         {
            "long_name": "2500",
            "short_name": "2500",
            "types": [
               "postal_code"
            ]
         },
         {
            "long_name": "West Wollongong",
            "short_name": "West Wollongong",
            "types": [
               "locality",
               "political"
            ]
         },
         {
            "long_name": "Wollongong City Council",
            "short_name": "Wollongong",
            "types": [
               "administrative_area_level_2",
               "political"
            ]
         },
         {
            "long_name": "New South Wales",
            "short_name": "NSW",
            "types": [
               "administrative_area_level_1",
               "political"
            ]
         },
         {
            "long_name": "Australia",
            "short_name": "AU",
            "types": [
               "country",
               "political"
            ]
         }
      ],
      "formatted_address": "West Wollongong NSW 2500, Australia",
      "geometry": {
         "bounds": {
            "northeast": {
               "lat": -34.37453,
               "lng": 150.91104
            },
            "southwest": {
               "lat": -34.46694,
               "lng": 150.82986
            }
         },
         "location": {
            "lat": -34.42071,
            "lng": 150.87839
         },
         "location_type": "APPROXIMATE",
         "viewport": {
            "northeast": {
               "lat": -34.37453,
               "lng": 150.91104
            },
            "southwest": {
               "lat": -34.46694,
               "lng": 150.82986
            }
         }
      },
      "place_id": "ChIJ-xkxwv0bE2sREIa6P2t9ARw",
      "postcode_localities": [
         "Coniston",
         "Gwynneville",
         "Keiraville",
         "Mangerton",
         "Mount Keira",
         "Mount Saint Thomas",
         "North Wollongong",
         "Spring Hill",
         "West Wollongong",
         "Wollongong"
      ],
      "types": [
         "postal_code"
      ]
   },
   {
      "address_components": [
         {
            "long_name": "Wollongong City Council",
            "short_name": "Wollongong",
            "types": [
               "administrative_area_level_2",
               "political"
            ]
         },
         {
            "long_name": "New South Wales",
            "short_name": "NSW",
            "types": [
               "administrative_area_level_1",
               "political"
            ]
         },
         {
            "long_name": "Australia",
            "short_name": "AU",
            "types": [
               "country",
               "political"
            ]
         }
      ],
      "formatted_address": "Wollongong, NSW, Australia",
      "geometry": {
         "bounds": {
            "northeast": {
               "lat": -34.130013,
               "lng": 151.06657
            },
            "southwest": {
               "lat": -34.553738,
               "lng": 150.6351
            }
         },
         "location": {
            "lat": -34.399002,
            "lng": 150.81442
         },
         "location_type": "APPROXIMATE",
         "viewport": {
            "northeast": {
               "lat": -34.13008,
               "lng": 151.0658
            },
            "southwest": {
               "lat": -34.553738,
               "lng": 150.6351
            }
         }
      },
      "place_id": "ChIJq88ZmCQcE2sRV6RG082xwM8",
      "types": [
         "administrative_area_level_2",
         "political"
      ]
   },
   {
      "address_components": [
         {
            "long_name": "New South Wales",
            "short_name": "NSW",
            "types": [
               "administrative_area_level_1",
               "political"
            ]
         },
         {
            "long_name": "Australia",
            "short_name": "AU",
            "types": [
               "country",
               "political"
            ]
         }
      ],
      "formatted_address": "New South Wales, Australia",
      "geometry": {
         "bounds": {
            "northeast": {
               "lat": -28.15702,
               "lng": 159.10544
            },
            "southwest": {
               "lat": -37.50528,
               "lng": 140.99928
            }
         },
         "location": {
            "lat": -31.253218,
            "lng": 146.9211
         },
         "location_type": "APPROXIMATE",
         "viewport": {
            "northeast": {
               "lat": -28.157072,
               "lng": 153.63852
            },
            "southwest": {
               "lat": -37.505016,
               "lng": 140.99928
            }
         }
      },
      "place_id": "ChIJDUte93TLDWsRLZ_EIhGvgBc",
      "types": [
         "administrative_area_level_1",
         "political"
      ]
   },
   {
      "address_components": [
         {
            "long_name": "Australia",
            "short_name": "AU",
            "types": [
               "country",
               "political"
            ]
         }
      ],
      "formatted_address": "Australia",
      "geometry": {
         "bounds": {
            "northeast": {
               "lat": -9.187026,
               "lng": 159.28722
            },
            "southwest": {
               "lat": -54.833767,
               "lng": 110.951035
            }
         },
         "location": {
            "lat": -25.274399,
            "lng": 133.77513
         },
         "location_type": "APPROXIMATE",
         "viewport": {
            "northeast": {
               "lat": -0.6911344,
               "lng": 166.74292
            },
            "southwest": {
               "lat": -51.663322,
               "lng": 100.09111
            }
         }
      },
      "place_id": "ChIJ38WHZwf9KysRUhNblaFnglM",
      "types": [
         "country",
         "political"
      ]
   }
]
```
