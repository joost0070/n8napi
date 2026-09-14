# Merk-configuratie: uitleg per veld

Dit bestand vult de "business-kennis" aan die niet uit ChannelEngine of Shopify
te halen is. Zonder deze regels kan het systeem wel *tellen*, maar niet
*oordelen*. Eén regel per merk.

| Veld | Wat vul je in | Waarom het systeem dit nodig heeft |
|---|---|---|
| `merk` | Exact zoals in ChannelEngine (veld `Brand` / extra-veld `merk`) | Koppelsleutel |
| `seizoen_type` | `FW`, `SS`, `FW+SS` of `ALL` (doorlopend) | Bepaalt of restvoorraad een probleem is of gewoon doorloopt |
| `fw_start_week` / `fw_eind_week` | ISO-weeknummers van het verkoopvenster herfst/winter | "Te veel" = meer dan je vóór `fw_eind_week` nog kwijt kunt |
| `ss_start_week` / `ss_eind_week` | Idem voor lente/zomer | Idem |
| `levertijd_dagen` | Dagen van bestellen tot op voorraad | Kernwaarde: signaal moet *minstens* zo ver vooruit |
| `nabestellen_mogelijk` | `ja` = NOOS/replenishment, `nee` = alleen voorseizoen-inkoop | Bij `nee` is een tekortsignaal informatief (afprijzen/spreiden), bij `ja` is het een bestelactie |
| `order_cutoff_fw` / `order_cutoff_ss` | Laatste besteldatum per seizoen | Na deze datum verandert het advies van "bijbestellen" naar "herverdelen/afprijzen" |
| `min_order_eenheid` | Minimum afname: los paar / size-run / doos van N | Adviesaantal moet hierop afgerond worden |
| `signaal_horizon_weken` | Hoeveel weken vooruit wil je gewaarschuwd worden | Default = `levertijd_dagen/7 + veiligheidsvoorraad_weken` |
| `veiligheidsvoorraad_weken` | Buffer bovenop levertijd | Vangt vraagpieken en leveronzekerheid op |
| `kernmaten` | Maten die altijd op voorraad horen (bv. `38-44`) | Een gat hier is duurder dan een gat in een randmaat |
| `maatcurve_bron` | `verkoop` (eigen historie) of `merk` (curve van leverancier) | Referentie waartegen scheefheid gemeten wordt |
| `markdown_week_fw` / `markdown_week_ss` | Week waarin dit merk in de sale mag | Bepaalt wanneer "afprijzen" een geldig advies is |
| `noos_lijst` | Artikelnummers die nooit uit voorraad mogen | Krijgen strengere drempel |
| `doel_sell_through_pct` | Gewenst % verkocht aan het eind van het seizoen | Meet of je op koers ligt |
| `max_woc` | Maximaal acceptabele weken voorraad | Boven deze grens = overstock-signaal |
| `retour_norm_pct` | Normaal retourpercentage voor dit merk | Boven de norm = maat-/pasvormprobleem, niet vraagprobleem |
| `opmerking` | Vrij veld | Bijv. "levert alleen 2x per jaar", "valt klein" |
