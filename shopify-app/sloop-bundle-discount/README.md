# Bline: Sloop bundelkorting (Shopify Function)

Discount function die 33% korting geeft op ALLE slopen in de winkelwagen
zodra er minimaal 1 leeskussen in zit. Onbeperkt aantal slopen (de native
BXGY-korting kan maximaal 2 per kussen).

## Wat hier staat

- `shopify.app.toml`: gekoppeld aan de bestaande "Bline API" custom app
- `extensions/sloop-bundle-discount/`: de discount function
  - `src/cart_lines_discounts_generate_run.graphql`: input (checkt per regel
    of het product in collectie Leeskussens of Leeskussen slopen zit)
  - `src/cart_lines_discounts_generate_run.js`: de logica

## Deployen (eenmalig, ~5 min)

Vereist: Node 20+, Shopify CLI (`npm i -g @shopify/cli`), en een CLI-token
uit het Dev Dashboard (dev.shopify.com, organisatie-instellingen, CLI tokens)
als je headless deployt. Interactief kan ook gewoon met browser-login.

```bash
cd shopify-app/sloop-bundle-discount
npm i -g @shopify/cli
shopify app deploy   # kies/bevestig de app "Bline API"
```

## Na de deploy: korting activeren + oude BXGY uitzetten

1. Haal de function-id op (Admin GraphQL):

```graphql
{ shopifyFunctions(first: 10) { nodes { id title apiType } } }
```

2. Maak de automatische korting aan:

```graphql
mutation {
  discountAutomaticAppCreate(automaticAppDiscount: {
    title: "Bundel: 33% korting op alle hoezen",
    functionId: "<FUNCTION_ID>",
    startsAt: "2026-07-01T00:00:00Z",
    discountClasses: [PRODUCT]
  }) { userErrors { field message } }
}
```

3. Deactiveer daarna de bestaande BXGY-korting
   (DiscountAutomaticNode/2264263393629) via `discountAutomaticDeactivate`,
   anders stapelen ze.

4. Pas in het thema de widget-berekening aan:
   in `sections/product-main.liquid` de regel met `Math.min(totalHoezen,
   kussenQty * 2)` terugzetten naar `totalHoezen` (en in
   `product-main-slopen.liquid` idem `hoesQty`), zodat de preview weer
   "elke hoes 33%" toont.
