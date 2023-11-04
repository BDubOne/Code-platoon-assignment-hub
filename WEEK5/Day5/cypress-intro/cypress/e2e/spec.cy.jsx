describe('template spec', () => {
  it('passes', () => {
    cy.visit('https://example.cypress.io')
  })
})

describe('My First Cypress Test', () => {
  it('Visits the app and asserts title', () => {
    cy.visit('/');
    for(let i = 0; i < 5; i++){
    cy.get("#theButton").click()
    }
    // Replace with your app's URL
    cy.get('h1').should('contain', 'Vite + React'); // Adjust the selector and text as needed
  });
});