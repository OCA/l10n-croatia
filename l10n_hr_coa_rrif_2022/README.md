# RRIF 2021 Chart of accounts

Update 9.1.2023:

Tax report lines adjusted to lates TAX report schema valid from 3.1.2023 items in
section VI are not fully tested and are subject to implementation.

Update 26.12.2022:

As odoo shows no interes in merging this module to core odoo, authors decided to publish
it under OCA repo

Update 18.12.2022:

- as of 30.11. Vat on payment has to be processed in same manner on vendor bills
- Look for : Porez na dodanu vrijednost - Odbitak pretporeza Broj klase:410-19/22-02/87
  Urudžbeni broj:513-07-21-01-22-3, Zagreb, 30.11.2022
- https://www.porezna-uprava.hr/HR_publikacije/Lists/mislenje33/Display.aspx?id=19808

- DEVDLOPMENT NOTES - will be cleaned before final merge
  - cross compared two simmilar croatian localisation PRs:

1. odoo-dev (@malb-odoo) : https://github.com/odoo/odoo/pull/99450

   - internal odoo development, without good knowledge of terms (google translate is our
     friend but may lead to missconfiguration)

2. dajmi5 (@bad_bole) : https://github.com/odoo/odoo/pull/102018

   - croatian development, involving several developers with experience

What is done in this branch (in file load order):

- adopted new short external ids terminology/logic from odoo developers

1. account.account.template

   - added more accounts needed for regular postings
   - some lvl3 accounts from odoo-dev replaced by more detailed level accounts
   - added some 3rd level accounts missing

2. account.group.template

   - odoo-dev accounts groups was 2 level based, while in Croatia it is more common to
     use 3 levels
   - all 3rd lvl groups are added with structure, not visible on widget, but corectly
     used and assigned on account creation from form view.

3. account.tax.group

   - only 4 groups, fine!

4. account_chart_tag_data

   - modified according to created accounts

5. account_tax_report

   - modified/simplified external ids
   - addopted new structure from odoo-dev

6. acount.tax.template

   - added more taxes to fit all fiscal positions
   - will probabla need to add a few more taxes
   - modified tax names and labels to more unified look and feel
   - improoved tax usage atributes
   - translations (english terms tranlsated better)
   - croatia translations might need corrections

7. account.fiscal.position.template

   - instead of creating 2 or 3 separate files for : fp.template , fp.tax.template and
     fp.acc_template objects
   - created one file, applied nested xml data logic, wich is more readable to
     developers.
   - created common Croatia fiscal positions, with tax and account mappings
   - might need updates

- Files used for this localisation by odoo dev team:

  - https://www.rrif.hr/dok/preuzimanje/Bilanca-2016.pdf
  - https://www.rrif.hr/dok/preuzimanje/RRIF-RP2021.PDF
  - https://www.rrif.hr/dok/preuzimanje/RRIF-RP2021-ENG.PDF

- Additional files suggested for developers:

  - https://www.rrif.hr/dok/preuzimanje/RRIF-RP2021.7z

- Chart of Accounts (RRIF ver.2021)

  - Short version of RRIF 2021 CoA

    - odoo developed too small so this version is extended for some more needed accounts

  - Account groups -
    - odoo dev based on 2 level is improoved by adding 3rd lvl account groups

- Lines of TAX REPORT

  - source PDV report :
    https://www.porezna-uprava.hr/HR_obrasci/Documents/POREZ%20NA%20DODANU%20VRIJEDNOST/PDV.pdf

- Taxes according to tax report lines, and some additional not in tax reprot

  - Tax report section I - tax exept or ili 0% tax
    - 0% Domestic Reverse charge / 0% Tuzemni PPO
    - 0% Deliveries in another EU member state / 0% ISP.U DR.DRŽ.ČLANICAMA
    - 0% Sale goods in EU / 0% DOBRA EU
    - 0% Sale service in EU / USLUGE EU
    - 0% Deliveries to non residents / 0% BEZ SJEDIŠTA
    - 0% install and assemble in EU state / 0% SAST/POST EU
    - 0% delivery of new vehicles to EU / 0% PRIJEVOZNA SREDSTVA EU
    - 0% 0% Domestic deliveries / TUZEMNE ISP.
    - 0% IZVOZNE ISP.
    - 0% OSTALA OSLOBOĐENJA
  - PDV-II - oporezive transakcije - Isporuke
    - 25% PDV na Dobra
    - 25% PDV na Usluge
    - 25% PDV na Predujam
    - 13% PDV Dobra
    - 13% PDV Usluge
    - 13% PDV na Predujam
    - 5% PDV na Dobra
    - 5% PDV na Predujam
  - PDV-III - obračunati pretporez - Nabava
    - PPDV 25% na Dobra
    - PPDV 25% Usluge
    - PPDV 25% na Predujam
    - PPDV 25% po naplaćenom
    - PPDV 13% na Dobra
    - PPDV 13% Usluge
    - PPDV 13% na Predujam
    - PPDV 5% na Dobra
    - PPDV 5% na Predujam
  - PDV III-II - reverse charge - Nabava
    - Prijenos PO 25% ( PPO PP 25% - PPO PDV 25% )
    - EU 5% DOBRA ( EU PP 5% na dobra - EU PDV 5% na Dobra )
    - EU 13% DOBRA ( EU PP 13% na dobra - EU PDV 13% na Dobra )
    - EU 25% DOBRA ( EU PP 25% na Dobra - EU PDV 25% na Dobra )
    - EU 25% USLUGE ( EU PP 25% na Usluge - EU PDV 25% na Usluge )
    - Bez sjedišta 25% ( Bez sjedišta PP 25% - Bez sjedišta PDV 25% )(13%,5%)
    - UVOZ 25% ( Uvoz PP 25% - Uvoz PDV 25% ) (13%,5%)

- Osnovne fiskalne pozicije
  - R1 partneri
  - EU Partneri
  - INO partneri
  - Kupci Građani
  - R2 partneri
  - AVANS
  - Prijenos PO
  - Bez sjedista
