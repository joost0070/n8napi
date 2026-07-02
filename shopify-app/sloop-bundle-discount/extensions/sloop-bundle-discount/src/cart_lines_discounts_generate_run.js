// Bline bundelkorting: zit er een leeskussen in de winkelwagen,
// dan krijgt ELKE sloop in de winkelwagen 33% korting (onbeperkt aantal).
export function cartLinesDiscountsGenerateRun(input) {
  if (!input.discount.discountClasses.includes("PRODUCT")) {
    return { operations: [] };
  }

  const lines = input.cart.lines.filter(
    (line) => line.merchandise.__typename === "ProductVariant",
  );

  const hasKussen = lines.some((line) => line.merchandise.product.isKussen);
  if (!hasKussen) {
    return { operations: [] };
  }

  const candidates = lines
    .filter((line) => line.merchandise.product.isSloop)
    .map((line) => ({
      message: "Bundelkorting: 33% op je hoes",
      targets: [{ cartLine: { id: line.id } }],
      value: { percentage: { value: 33 } },
    }));

  if (candidates.length === 0) {
    return { operations: [] };
  }

  return {
    operations: [
      {
        productDiscountsAdd: {
          candidates,
          selectionStrategy: "ALL",
        },
      },
    ],
  };
}
