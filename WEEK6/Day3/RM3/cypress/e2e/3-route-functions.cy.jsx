describe("Header.jsx", () => {
    it("check all links are available to the correct routes", () => {
      cy.visit("http://localhost:5173/");
  
      cy.get("a.nav-link")
        .eq(1)
        .should("contain.text", "Characters")
        .should("have.attr", "href", "/characters/");
        cy.get('a.nav-link').eq(1)
        .click()

      cy.get('.card').eq(1)
      .should('contain', '.card-body')
    //   cy.get('button').eq(0)
    })

})