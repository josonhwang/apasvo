# -*- coding: utf-8 -*-

# Resource object code
#
# Created: Fri Apr 4 00:11:34 2014
#      by: The Resource Compiler for PySide (Qt v4.8.0)
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore

qt_resource_data = "\x00\x00\x09\x97<!DOCTYPE html>\x0a\x0a<html>\x0a<head>\x0a\x09<meta charset=\x22utf-8\x22 />\x0a\x09<title>Application Info</title>\x0a\x09<style type=\x22text/css\x22>\x0a\x09body {\x0a\x09    text-align:center}\x0a\x09.reference {\x0a\x09    font-style: italic}\x0a\x09</style>\x0a</head>\x0a\x0a<body>\x0a<h1>EQ Picker Tool v.0.0.1</h1>\x0a\x0a<p>A graphical tool to perform event detection/picking over a seismic trace.</p>\x0a\x0a<p>Three different picking algorithms are available: STA-LTA, AMPA and Takanami</p>\x0a\x0a<p>\x0a    STA-LTA algorithm processes seismic signals by using two moving time\x0a    windows, a short time average window (STA), which measures the instant\x0a    amplitude of the signal and watches for earthquakes, and a long time\x0a    average windows, which takes care of the current average of the signal\x0a    amplitude.\x0a\x0a    <div class=reference>\x0a    See:\x0a    Trnkoczy, A. (2002). Understanding and parameter setting of STA/LTA trigger\x0a    algorithm. IASPEI New Manual of Seismological Observatory Practice, 2, 1-19.\x0a    </div>\x0a</p>\x0a\x0a<p>\x0a    Adaptive Multi-Band Picking Algorithm (AMPA) method consists on an\x0a    adaptive multi-band analysis that includes envelope detection, noise\x0a    reduction for each band, and finally a filter stage that enhances the\x0a    response to an earthquake arrival. This approach provides accurate\x0a    estimation of phase arrivals in seismic signals strongly affected by\x0a    background and non-stationary noises.\x0a    \x0a   <div class=reference>\x0a    See:\x0a    &Aacute;lvarez, I., Garc&iacute;a, L., Mota, S., Cort&eacute;s, G., Ben&iacute;tez, C.,\x0a    & De la Torre, A. (2013).\x0a    An Automatic P-Phase Picking Algorithm Based on Adaptive Multiband Processing.\x0a    Geoscience and Remote Sensing Letters, IEEE,\x0a    Volume: 10, Issue: 6, pp. 1488 - 1492\x0a    </div>\x0a</p>\x0a\x0a<p>\x0a    Takanami algorithm estimates the arrival time of a seismic signal\x0a    by using two autoregressive models: a model that fits the earthquake and\x0a    a noise model. Assuming that the characteristics before and after the\x0a    arrival of the earthquake are quite different, the arrival time is\x0a    estimated by searching the time point where the minimum value of the\x0a    Akaike's Information Criterion is reached.\x0a\x0a   <div class=reference>\x0a    See:\x0a    Takanami, T., & Kitagawa, G. (1988).\x0a    A new efficient procedure for the estimation of onset times of seismic\x0a    waves. Journal of Physics of the Earth, 36(6), 267-290.\x0a    </div>\x0a</p>\x0a\x0a\x0a<p>Created by Jose Emilio Romero Lopez.</p>\x0a<p>Copyright 2013-2014. All rights reserved.</p>\x0a</body>\x0a\x0a</html>\x00\x00\x1d\xe3                   GNU LESSER GENERAL PUBLIC LICENSE\x0a                       Version 3, 29 June 2007\x0a\x0a Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>\x0a Everyone is permitted to copy and distribute verbatim copies\x0a of this license document, but changing it is not allowed.\x0a\x0a\x0a  This version of the GNU Lesser General Public License incorporates\x0athe terms and conditions of version 3 of the GNU General Public\x0aLicense, supplemented by the additional permissions listed below.\x0a\x0a  0. Additional Definitions.\x0a\x0a  As used herein, \x22this License\x22 refers to version 3 of the GNU Lesser\x0aGeneral Public License, and the \x22GNU GPL\x22 refers to version 3 of the GNU\x0aGeneral Public License.\x0a\x0a  \x22The Library\x22 refers to a covered work governed by this License,\x0aother than an Application or a Combined Work as defined below.\x0a\x0a  An \x22Application\x22 is any work that makes use of an interface provided\x0aby the Library, but which is not otherwise based on the Library.\x0aDefining a subclass of a class defined by the Library is deemed a mode\x0aof using an interface provided by the Library.\x0a\x0a  A \x22Combined Work\x22 is a work produced by combining or linking an\x0aApplication with the Library.  The particular version of the Library\x0awith which the Combined Work was made is also called the \x22Linked\x0aVersion\x22.\x0a\x0a  The \x22Minimal Corresponding Source\x22 for a Combined Work means the\x0aCorresponding Source for the Combined Work, excluding any source code\x0afor portions of the Combined Work that, considered in isolation, are\x0abased on the Application, and not on the Linked Version.\x0a\x0a  The \x22Corresponding Application Code\x22 for a Combined Work means the\x0aobject code and/or source code for the Application, including any data\x0aand utility programs needed for reproducing the Combined Work from the\x0aApplication, but excluding the System Libraries of the Combined Work.\x0a\x0a  1. Exception to Section 3 of the GNU GPL.\x0a\x0a  You may convey a covered work under sections 3 and 4 of this License\x0awithout being bound by section 3 of the GNU GPL.\x0a\x0a  2. Conveying Modified Versions.\x0a\x0a  If you modify a copy of the Library, and, in your modifications, a\x0afacility refers to a function or data to be supplied by an Application\x0athat uses the facility (other than as an argument passed when the\x0afacility is invoked), then you may convey a copy of the modified\x0aversion:\x0a\x0a   a) under this License, provided that you make a good faith effort to\x0a   ensure that, in the event an Application does not supply the\x0a   function or data, the facility still operates, and performs\x0a   whatever part of its purpose remains meaningful, or\x0a\x0a   b) under the GNU GPL, with none of the additional permissions of\x0a   this License applicable to that copy.\x0a\x0a  3. Object Code Incorporating Material from Library Header Files.\x0a\x0a  The object code form of an Application may incorporate material from\x0aa header file that is part of the Library.  You may convey such object\x0acode under terms of your choice, provided that, if the incorporated\x0amaterial is not limited to numerical parameters, data structure\x0alayouts and accessors, or small macros, inline functions and templates\x0a(ten or fewer lines in length), you do both of the following:\x0a\x0a   a) Give prominent notice with each copy of the object code that the\x0a   Library is used in it and that the Library and its use are\x0a   covered by this License.\x0a\x0a   b) Accompany the object code with a copy of the GNU GPL and this license\x0a   document.\x0a\x0a  4. Combined Works.\x0a\x0a  You may convey a Combined Work under terms of your choice that,\x0ataken together, effectively do not restrict modification of the\x0aportions of the Library contained in the Combined Work and reverse\x0aengineering for debugging such modifications, if you also do each of\x0athe following:\x0a\x0a   a) Give prominent notice with each copy of the Combined Work that\x0a   the Library is used in it and that the Library and its use are\x0a   covered by this License.\x0a\x0a   b) Accompany the Combined Work with a copy of the GNU GPL and this license\x0a   document.\x0a\x0a   c) For a Combined Work that displays copyright notices during\x0a   execution, include the copyright notice for the Library among\x0a   these notices, as well as a reference directing the user to the\x0a   copies of the GNU GPL and this license document.\x0a\x0a   d) Do one of the following:\x0a\x0a       0) Convey the Minimal Corresponding Source under the terms of this\x0a       License, and the Corresponding Application Code in a form\x0a       suitable for, and under terms that permit, the user to\x0a       recombine or relink the Application with a modified version of\x0a       the Linked Version to produce a modified Combined Work, in the\x0a       manner specified by section 6 of the GNU GPL for conveying\x0a       Corresponding Source.\x0a\x0a       1) Use a suitable shared library mechanism for linking with the\x0a       Library.  A suitable mechanism is one that (a) uses at run time\x0a       a copy of the Library already present on the user's computer\x0a       system, and (b) will operate properly with a modified version\x0a       of the Library that is interface-compatible with the Linked\x0a       Version.\x0a\x0a   e) Provide Installation Information, but only if you would otherwise\x0a   be required to provide such information under section 6 of the\x0a   GNU GPL, and only to the extent that such information is\x0a   necessary to install and execute a modified version of the\x0a   Combined Work produced by recombining or relinking the\x0a   Application with a modified version of the Linked Version. (If\x0a   you use option 4d0, the Installation Information must accompany\x0a   the Minimal Corresponding Source and Corresponding Application\x0a   Code. If you use option 4d1, you must provide the Installation\x0a   Information in the manner specified by section 6 of the GNU GPL\x0a   for conveying Corresponding Source.)\x0a\x0a  5. Combined Libraries.\x0a\x0a  You may place library facilities that are a work based on the\x0aLibrary side by side in a single library together with other library\x0afacilities that are not Applications and are not covered by this\x0aLicense, and convey such a combined library under terms of your\x0achoice, if you do both of the following:\x0a\x0a   a) Accompany the combined library with a copy of the same work based\x0a   on the Library, uncombined with any other library facilities,\x0a   conveyed under the terms of this License.\x0a\x0a   b) Give prominent notice with the combined library that part of it\x0a   is a work based on the Library, and explaining where to find the\x0a   accompanying uncombined form of the same work.\x0a\x0a  6. Revised Versions of the GNU Lesser General Public License.\x0a\x0a  The Free Software Foundation may publish revised and/or new versions\x0aof the GNU Lesser General Public License from time to time. Such new\x0aversions will be similar in spirit to the present version, but may\x0adiffer in detail to address new problems or concerns.\x0a\x0a  Each version is given a distinguishing version number. If the\x0aLibrary as you received it specifies that a certain numbered version\x0aof the GNU Lesser General Public License \x22or any later version\x22\x0aapplies to it, you have the option of following the terms and\x0aconditions either of that published version or of any later version\x0apublished by the Free Software Foundation. If the Library as you\x0areceived it does not specify a version number of the GNU Lesser\x0aGeneral Public License, you may choose any version of the GNU Lesser\x0aGeneral Public License ever published by the Free Software Foundation.\x0a\x0a  If the Library as you received it specifies that a proxy can decide\x0awhether future versions of the GNU Lesser General Public License shall\x0aapply, that proxy's public statement of acceptance of any version is\x0apermanent authorization for you to choose that version for the\x0aLibrary.\x0a"
qt_resource_name = "\x00\x0c\x0d\x8d\xcf<\x00v\x00e\x00r\x00s\x00i\x00o\x00n\x00.\x00h\x00t\x00m\x00l\x00\x0b\x05u\xa8t\x00l\x00i\x00c\x00e\x00n\x00s\x00e\x00.\x00t\x00x\x00t"
qt_resource_struct = "\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x1e\x00\x00\x00\x00\x00\x01\x00\x00\x09\x9b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00"
def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
