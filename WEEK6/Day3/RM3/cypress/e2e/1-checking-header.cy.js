describe("Header.jsx", () => {
  it("check all links are available to the correct routes", () => {
    cy.visit("http://localhost:5173/");

    cy.get("a.nav-link")
      .eq(1)
      .should("contain.text", "Characters")
      .should("have.attr", "href", "/characters/");

    cy.get("a.nav-link")
      .eq(0)
      .should("contain.text", "About")
      .should("have.attr", "href", "/about/");

    cy.get("a.nav-link")
      .eq(2)
      .should("contain.text", "Favorites")
      .should("have.attr", "href", "/favorites/");

      cy.get("input")
      .should("exist")
      .type("rick sanchez")
      .should('have.value', 'rick sanchez')

      cy.get('#search-button')
      .click()
      cy.url().should('contain', '/search-results/')

      cy.get('.card')
      cy.get('.card').should('contain', "Rick Sanchez")
    });
  });


  // <button type="submit" class="btn btn-primary">Search</button>