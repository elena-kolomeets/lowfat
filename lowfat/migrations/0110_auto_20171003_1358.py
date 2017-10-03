# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 13:58
from __future__ import unicode_literals

from django.db import migrations, models

def fix_jacs_code(apps, schema_editor):
    Claimant = apps.get_model("lowfat", "Claimant")
    for claimant in Claimant.objects.all():
        claimant.research_area_code = claimant.research_area_code[0:2]
        claimant.save()

def reverse_fix_jacs_code(apps, schema_editor):
    Claimant = apps.get_model("lowfat", "Claimant")
    for claimant in Claimant.objects.all():
        claimant.research_area_code = "{}00".format(claimant.research_area_code)
        claimant.save()

class Migration(migrations.Migration):

    dependencies = [
        ('lowfat', '0109_auto_20170921_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claimant',
            name='research_area_code',
            field=models.CharField(choices=[('A0', '(A0) Broadly-based programmes within medicine & dentistry'), ('A1', '(A1) Pre-clinical medicine'), ('A2', '(A2) Pre-clinical dentistry'), ('A3', '(A3) Clinical medicine'), ('A4', '(A4) Clinical dentistry'), ('A9', '(A9) Others in medicine & dentistry'), ('B0', '(B0) Broadly-based programmes within subjects allied to medicine'), ('B1', '(B1) Anatomy, physiology & pathology'), ('B2', '(B2) Pharmacology, toxicology & pharmacy'), ('B3', '(B3) Complementary medicines, therapies & well-being'), ('B4', '(B4) Nutrition'), ('B5', '(B5) Ophthalmics'), ('B6', '(B6) Aural & oral sciences'), ('B7', '(B7) Nursing'), ('B8', '(B8) Medical technology'), ('B9', '(B9) Others in subjects allied to medicine'), ('C0', '(C0) Broadly-based programmes within biological sciences'), ('C1', '(C1) Biology'), ('C2', '(C2) Botany'), ('C3', '(C3) Zoology'), ('C4', '(C4) Genetics'), ('C5', '(C5) Microbiology'), ('C6', '(C6) Sport & exercise science'), ('C7', '(C7) Molecular biology, biophysics & biochemistry'), ('C8', '(C8) Psychology'), ('C9', '(C9) Others in Biological Sciences'), ('D1', '(D1) Pre-clinical veterinary medicine'), ('D2', '(D2) Clinical veterinary medicine & dentistry'), ('D0', '(D0) Broadly-based programmes within agriculture & related subjects'), ('D3', '(D3) Animal science'), ('D4', '(D4) Agriculture'), ('D5', '(D5) Forestry & arboriculture'), ('D6', '(D6) Food & beverage studies'), ('D7', '(D7) Agricultural sciences'), ('D9', '(D9) Others in veterinary sciences, agriculture & related subjects'), ('F0', '(F0) Broadly-based programmes within physical sciences'), ('F1', '(F1) Chemistry'), ('F2', '(F2) Materials science'), ('F3', '(F3) Physics'), ('F4', '(F4) Forensic & archaeological sciences'), ('F5', '(F5) Astronomy'), ('F6', '(F6) Geology'), ('F7', '(F7) Science of aquatic & terrestrial environments'), ('F8', '(F8) Physical geographical sciences'), ('F9', '(F9) Others in physical sciences'), ('G1', '(G1) Mathematics'), ('G2', '(G2) Operational research'), ('G3', '(G3) Statistics'), ('G9', '(G9) Others in mathematical sciences'), ('I1', '(I1) Computer science'), ('I2', '(I2) Information systems'), ('I3', '(I3) Software engineering'), ('I4', '(I4) Artificial intelligence'), ('I5', '(I5) Health informatics'), ('I6', '(I6) Games'), ('I7', '(I7) Computer generated visual & audio effects'), ('I9', '(I9) Others in Computer sciences'), ('H0', '(H0) Broadly-based programmes within engineering & technology'), ('H1', '(H1) General engineering'), ('H2', '(H2) Civil engineering'), ('H3', '(H3) Mechanical engineering'), ('H4', '(H4) Aerospace engineering'), ('H5', '(H5) Naval architecture'), ('H6', '(H6) Electronic & electrical engineering'), ('H7', '(H7) Production & manufacturing engineering'), ('H8', '(H8) Chemical, process & energy engineering'), ('H9', '(H9) Others in engineering'), ('J1', '(J1) Minerals technology'), ('J2', '(J2) Metallurgy'), ('J3', '(J3) Ceramics & glass'), ('J4', '(J4) Polymers & textiles'), ('J5', '(J5) Materials technology not otherwise specified'), ('J6', '(J6) Maritime technology'), ('J7', '(J7) Biotechnology'), ('J9', '(J9) Others in technology'), ('K0', '(K0) Broadly-based programmes within architecture, building & planning'), ('K1', '(K1) Architecture'), ('K2', '(K2) Building'), ('K3', '(K3) Landscape & garden design'), ('K4', '(K4) Planning (urban, rural & regional)'), ('K9', '(K9) Others in architecture, building & planning'), ('L0', '(L0) Broadly-based programmes within social studies'), ('L1', '(L1) Economics'), ('L2', '(L2) Politics'), ('L3', '(L3) Sociology'), ('L4', '(L4) Social policy'), ('L5', '(L5) Social work'), ('L6', '(L6) Anthropology'), ('L7', '(L7) Human & social geography'), ('L8', '(L8) Development studies'), ('L9', '(L9) Others in social studies'), ('M0', '(M0) Broadly-based programmes within law'), ('M1', '(M1) Law by area'), ('M2', '(M2) Law by topic'), ('M9', '(M9) Others in law'), ('N0', '(N0) Broadly-based programmes within business & administrative studies'), ('N1', '(N1) Business studies'), ('N2', '(N2) Management studies'), ('N3', '(N3) Finance'), ('N4', '(N4) Accounting'), ('N5', '(N5) Marketing'), ('N6', '(N6) Human resource management'), ('N7', '(N7) Office skills'), ('N8', '(N8) Hospitality, leisure, sport, tourism & transport'), ('N9', '(N9) Others in business & administrative studies'), ('P0', '(P0) Broadly-based programmes within mass communications & documentation'), ('P1', '(P1) Information services'), ('P2', '(P2) Publicity studies'), ('P3', '(P3) Media studies'), ('P4', '(P4) Publishing'), ('P5', '(P5) Journalism'), ('P9', '(P9) Others in mass communications & documentation'), ('Q0', '(Q0) Broadly-based programmes within languages'), ('Q1', '(Q1) Linguistics'), ('Q2', '(Q2) Comparative literary studies'), ('Q3', '(Q3) English studies'), ('Q4', '(Q4) Ancient language studies'), ('Q5', '(Q5) Celtic studies'), ('Q6', '(Q6) Latin studies'), ('Q7', '(Q7) Classical Greek studies'), ('Q8', '(Q8) Classical studies'), ('Q9', '(Q9) Others in linguistics, classics & related subjects'), ('R1', '(R1) French studies'), ('R2', '(R2) German studies'), ('R3', '(R3) Italian studies'), ('R4', '(R4) Spanish studies'), ('R5', '(R5) Portuguese studies'), ('R6', '(R6) Scandinavian studies'), ('R7', '(R7) Russian & East European studies'), ('R8', '(R8) European studies'), ('R9', '(R9) Others in European languages, literature & related subjects'), ('T1', '(T1) Chinese studies'), ('T2', '(T2) Japanese studies'), ('T3', '(T3) South Asian studies'), ('T4', '(T4) Other Asian studies'), ('T5', '(T5) African studies'), ('T6', '(T6) Modern Middle Eastern studies'), ('T7', '(T7) American studies'), ('T8', '(T8) Australasian studies'), ('T9', '(T9) Others in Eastern, Asiatic, African, American & Australasian languages, literature & related subjects'), ('V0', '(V0) Broadly-based programmes within historical & philosophical studies'), ('V1', '(V1) History by period'), ('V2', '(V2) History by area'), ('V3', '(V3) History by topic'), ('V4', '(V4) Archaeology'), ('V5', '(V5) Philosophy'), ('V6', '(V6) Theology & religious studies'), ('V7', '(V7) Heritage studies'), ('V9', '(V9) Others in historical & philosophical studies'), ('W0', '(W0) Broadly-based programmes within creative arts & design'), ('W1', '(W1) Fine art'), ('W2', '(W2) Design studies'), ('W3', '(W3) Music'), ('W4', '(W4) Drama'), ('W5', '(W5) Dance'), ('W6', '(W6) Cinematics & photography'), ('W7', '(W7) Crafts'), ('W8', '(W8) Imaginative writing'), ('W9', '(W9) Others in creative arts & design'), ('X0', '(X0) Broadly-based programmes within education'), ('X1', '(X1) Training teachers'), ('X2', '(X2) Research & study skills in education'), ('X3', '(X3) Academic studies in education'), ('X9', '(X9) Others in education'), ('Y0', '(Y0) Combined')], default='Y0', max_length=2),
        ),
        migrations.AlterField(
            model_name='historicalclaimant',
            name='research_area_code',
            field=models.CharField(choices=[('A0', '(A0) Broadly-based programmes within medicine & dentistry'), ('A1', '(A1) Pre-clinical medicine'), ('A2', '(A2) Pre-clinical dentistry'), ('A3', '(A3) Clinical medicine'), ('A4', '(A4) Clinical dentistry'), ('A9', '(A9) Others in medicine & dentistry'), ('B0', '(B0) Broadly-based programmes within subjects allied to medicine'), ('B1', '(B1) Anatomy, physiology & pathology'), ('B2', '(B2) Pharmacology, toxicology & pharmacy'), ('B3', '(B3) Complementary medicines, therapies & well-being'), ('B4', '(B4) Nutrition'), ('B5', '(B5) Ophthalmics'), ('B6', '(B6) Aural & oral sciences'), ('B7', '(B7) Nursing'), ('B8', '(B8) Medical technology'), ('B9', '(B9) Others in subjects allied to medicine'), ('C0', '(C0) Broadly-based programmes within biological sciences'), ('C1', '(C1) Biology'), ('C2', '(C2) Botany'), ('C3', '(C3) Zoology'), ('C4', '(C4) Genetics'), ('C5', '(C5) Microbiology'), ('C6', '(C6) Sport & exercise science'), ('C7', '(C7) Molecular biology, biophysics & biochemistry'), ('C8', '(C8) Psychology'), ('C9', '(C9) Others in Biological Sciences'), ('D1', '(D1) Pre-clinical veterinary medicine'), ('D2', '(D2) Clinical veterinary medicine & dentistry'), ('D0', '(D0) Broadly-based programmes within agriculture & related subjects'), ('D3', '(D3) Animal science'), ('D4', '(D4) Agriculture'), ('D5', '(D5) Forestry & arboriculture'), ('D6', '(D6) Food & beverage studies'), ('D7', '(D7) Agricultural sciences'), ('D9', '(D9) Others in veterinary sciences, agriculture & related subjects'), ('F0', '(F0) Broadly-based programmes within physical sciences'), ('F1', '(F1) Chemistry'), ('F2', '(F2) Materials science'), ('F3', '(F3) Physics'), ('F4', '(F4) Forensic & archaeological sciences'), ('F5', '(F5) Astronomy'), ('F6', '(F6) Geology'), ('F7', '(F7) Science of aquatic & terrestrial environments'), ('F8', '(F8) Physical geographical sciences'), ('F9', '(F9) Others in physical sciences'), ('G1', '(G1) Mathematics'), ('G2', '(G2) Operational research'), ('G3', '(G3) Statistics'), ('G9', '(G9) Others in mathematical sciences'), ('I1', '(I1) Computer science'), ('I2', '(I2) Information systems'), ('I3', '(I3) Software engineering'), ('I4', '(I4) Artificial intelligence'), ('I5', '(I5) Health informatics'), ('I6', '(I6) Games'), ('I7', '(I7) Computer generated visual & audio effects'), ('I9', '(I9) Others in Computer sciences'), ('H0', '(H0) Broadly-based programmes within engineering & technology'), ('H1', '(H1) General engineering'), ('H2', '(H2) Civil engineering'), ('H3', '(H3) Mechanical engineering'), ('H4', '(H4) Aerospace engineering'), ('H5', '(H5) Naval architecture'), ('H6', '(H6) Electronic & electrical engineering'), ('H7', '(H7) Production & manufacturing engineering'), ('H8', '(H8) Chemical, process & energy engineering'), ('H9', '(H9) Others in engineering'), ('J1', '(J1) Minerals technology'), ('J2', '(J2) Metallurgy'), ('J3', '(J3) Ceramics & glass'), ('J4', '(J4) Polymers & textiles'), ('J5', '(J5) Materials technology not otherwise specified'), ('J6', '(J6) Maritime technology'), ('J7', '(J7) Biotechnology'), ('J9', '(J9) Others in technology'), ('K0', '(K0) Broadly-based programmes within architecture, building & planning'), ('K1', '(K1) Architecture'), ('K2', '(K2) Building'), ('K3', '(K3) Landscape & garden design'), ('K4', '(K4) Planning (urban, rural & regional)'), ('K9', '(K9) Others in architecture, building & planning'), ('L0', '(L0) Broadly-based programmes within social studies'), ('L1', '(L1) Economics'), ('L2', '(L2) Politics'), ('L3', '(L3) Sociology'), ('L4', '(L4) Social policy'), ('L5', '(L5) Social work'), ('L6', '(L6) Anthropology'), ('L7', '(L7) Human & social geography'), ('L8', '(L8) Development studies'), ('L9', '(L9) Others in social studies'), ('M0', '(M0) Broadly-based programmes within law'), ('M1', '(M1) Law by area'), ('M2', '(M2) Law by topic'), ('M9', '(M9) Others in law'), ('N0', '(N0) Broadly-based programmes within business & administrative studies'), ('N1', '(N1) Business studies'), ('N2', '(N2) Management studies'), ('N3', '(N3) Finance'), ('N4', '(N4) Accounting'), ('N5', '(N5) Marketing'), ('N6', '(N6) Human resource management'), ('N7', '(N7) Office skills'), ('N8', '(N8) Hospitality, leisure, sport, tourism & transport'), ('N9', '(N9) Others in business & administrative studies'), ('P0', '(P0) Broadly-based programmes within mass communications & documentation'), ('P1', '(P1) Information services'), ('P2', '(P2) Publicity studies'), ('P3', '(P3) Media studies'), ('P4', '(P4) Publishing'), ('P5', '(P5) Journalism'), ('P9', '(P9) Others in mass communications & documentation'), ('Q0', '(Q0) Broadly-based programmes within languages'), ('Q1', '(Q1) Linguistics'), ('Q2', '(Q2) Comparative literary studies'), ('Q3', '(Q3) English studies'), ('Q4', '(Q4) Ancient language studies'), ('Q5', '(Q5) Celtic studies'), ('Q6', '(Q6) Latin studies'), ('Q7', '(Q7) Classical Greek studies'), ('Q8', '(Q8) Classical studies'), ('Q9', '(Q9) Others in linguistics, classics & related subjects'), ('R1', '(R1) French studies'), ('R2', '(R2) German studies'), ('R3', '(R3) Italian studies'), ('R4', '(R4) Spanish studies'), ('R5', '(R5) Portuguese studies'), ('R6', '(R6) Scandinavian studies'), ('R7', '(R7) Russian & East European studies'), ('R8', '(R8) European studies'), ('R9', '(R9) Others in European languages, literature & related subjects'), ('T1', '(T1) Chinese studies'), ('T2', '(T2) Japanese studies'), ('T3', '(T3) South Asian studies'), ('T4', '(T4) Other Asian studies'), ('T5', '(T5) African studies'), ('T6', '(T6) Modern Middle Eastern studies'), ('T7', '(T7) American studies'), ('T8', '(T8) Australasian studies'), ('T9', '(T9) Others in Eastern, Asiatic, African, American & Australasian languages, literature & related subjects'), ('V0', '(V0) Broadly-based programmes within historical & philosophical studies'), ('V1', '(V1) History by period'), ('V2', '(V2) History by area'), ('V3', '(V3) History by topic'), ('V4', '(V4) Archaeology'), ('V5', '(V5) Philosophy'), ('V6', '(V6) Theology & religious studies'), ('V7', '(V7) Heritage studies'), ('V9', '(V9) Others in historical & philosophical studies'), ('W0', '(W0) Broadly-based programmes within creative arts & design'), ('W1', '(W1) Fine art'), ('W2', '(W2) Design studies'), ('W3', '(W3) Music'), ('W4', '(W4) Drama'), ('W5', '(W5) Dance'), ('W6', '(W6) Cinematics & photography'), ('W7', '(W7) Crafts'), ('W8', '(W8) Imaginative writing'), ('W9', '(W9) Others in creative arts & design'), ('X0', '(X0) Broadly-based programmes within education'), ('X1', '(X1) Training teachers'), ('X2', '(X2) Research & study skills in education'), ('X3', '(X3) Academic studies in education'), ('X9', '(X9) Others in education'), ('Y0', '(Y0) Combined')], default='Y0', max_length=2),
        ),
        migrations.RunPython(
            fix_jacs_code,
            reverse_fix_jacs_code
        ),
    ]
