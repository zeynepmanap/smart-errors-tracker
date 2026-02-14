{\rtf1\ansi\ansicpg1254\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from app import app, db, Error\
import random\
\
titles = [\
    "Database Timeout",\
    "API Connection Failed",\
    "Null Pointer Exception",\
    "Memory Leak Detected",\
    "Authentication Error",\
    "Permission Denied",\
    "Server Overload",\
    "Cache Miss Error",\
    "Payment Gateway Error",\
    "File Upload Failed"\
]\
\
descriptions = [\
    "Sistem beklenmeyen \uc0\u351 ekilde hata verdi.",\
    "Ba\uc0\u287 lant\u305  kurulamad\u305 .",\
    "Veri \'e7ekilirken sorun olu\uc0\u351 tu.",\
    "Timeout s\'fcresi a\uc0\u351 \u305 ld\u305 .",\
    "Yetki kontrol\'fc ba\uc0\u351 ar\u305 s\u305 z.",\
    "Sunucu cevap vermiyor.",\
    "\uc0\u304 \u351 lem yar\u305 da kesildi.",\
    "Servis ge\'e7ici olarak kapal\uc0\u305 .",\
    "Veri kayd\uc0\u305  ba\u351 ar\u305 s\u305 z.",\
    "Beklenmeyen istisna olu\uc0\u351 tu."\
]\
\
levels = ["D\'fc\uc0\u351 \'fck", "Orta", "Y\'fcksek"]\
\
with app.app_context():\
    for i in range(50):   # 50 hata ekleyecek\
        error = Error(\
            title=random.choice(titles),\
            description=random.choice(descriptions),\
            level=random.choice(levels)\
        )\
        db.session.add(error)\
\
    db.session.commit()\
\
print("\uc0\u55357 \u56613  50 adet hata ba\u351 ar\u305 yla eklendi!")\
}