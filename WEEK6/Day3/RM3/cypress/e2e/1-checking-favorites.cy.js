describe('FavoritesPage.jsx', () => {
    it("check adding and removing", () => {
        cy.visit('http://localhost:5173/characters/')

        cy.get('.btn-warning')
      
        .eq(0)
        .click()
        cy.get('.btn-warning')
        .eq(1)
        .click()
        cy.get('.btn-warning')
        .eq(2)
        .click()
        cy.get('.btn-warning')
        .eq(3)
        .click()

        cy.visit('http://localhost:5173/favorites/')
        .get('.card')
    })
})