Feature: Login

  Background:
    Given que abro el navegador en la página de login

  @smoke
  Scenario: Abrir Saucedemo
    Then el titulo contiene "Swag Labs"

  @e2e
  Scenario Outline: Login con combinacion de credenciales
    When inicion de sesion con "<usuario>" y "<password>"
    Then el resultado debe ser "<resultado>"
    Examples:
      | usuario         | password     | resultado |
      | standard_user   | secret_sauce | success   |
      | locked_out_user | secret_sauce | locked    |
      | standard_user   | bade_pass    | badcreds  |
