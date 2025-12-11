# HTTP Server TDD Practice Questions

## Exercise 1

Create `server_test.go` with a test for `PlayerServer` that expects to get Pepper's score as "20".

## Exercise 2

Create `server.go` with an empty `PlayerServer` function to satisfy the compiler's "undefined: PlayerServer" error.

## Exercise 3

The compiler says "too many arguments". Add the correct parameters to `PlayerServer`.

## Exercise 4

Make `PlayerServer` return "20" to pass the test.

## Exercise 5

Create `main.go` that wires up `PlayerServer` as an HTTP handler on port 5000.

## Exercise 6

Add a subtest for Floyd's score (expected: "10") to break the hard-coded approach.

## Exercise 7

Update `PlayerServer` to parse the player name from the URL and return different scores for Pepper and Floyd.

## Exercise 8

Refactor by extracting score retrieval into a separate `GetPlayerScore` function.

## Exercise 9

DRY up the tests by creating `newGetScoreRequest` and `assertResponseBody` helpers.

## Exercise 10

Create a `PlayerStore` interface with a `GetPlayerScore` method.

## Exercise 11

Convert `PlayerServer` from a function to a struct that holds a `PlayerStore`.

## Exercise 12

Add a `ServeHTTP` method to `PlayerServer` that implements the `Handler` interface.

## Exercise 13

Update tests to create a `PlayerServer` instance and call `ServeHTTP`.

## Exercise 14

Update `main.go` to create a `PlayerServer` struct instance.

## Exercise 15

Create a `StubPlayerStore` struct that implements `PlayerStore` using a map.

## Exercise 16

Create a `StubPlayerStore` with test data and inject it into `PlayerServer`.

## Exercise 17

Create a minimal `InMemoryPlayerStore` in `main.go` that returns a hard-coded value.

## Exercise 18

Add a test case that expects 404 status for a player not in the store.

## Exercise 19

Make the test pass by writing `StatusNotFound` on all responses (intentionally wrong to highlight test gaps).

## Exercise 20

Update all test cases to assert status codes and create an `assertStatus` helper.

## Exercise 21

Update `ServeHTTP` to only return 404 when score is 0.

## Exercise 22

Write a test for `POST /players/{name}` that expects `StatusAccepted`.

## Exercise 23

Add an `if` statement to check for POST method and return `StatusAccepted`.

## Exercise 24

Refactor `ServeHTTP` to use a switch statement and extract `processWin` and `showScore` methods.

## Exercise 25

Extend `StubPlayerStore` with a `winCalls` slice and `RecordWin` method to spy on calls.

## Exercise 26

Update `TestStoreWins` to verify that `RecordWin` is called once on POST. Add `newPostWinRequest` helper.

## Exercise 27

Fix struct initializer errors by adding `nil` for the new `winCalls` field.

## Exercise 28

Add `RecordWin(name string)` to the `PlayerStore` interface.

## Exercise 29

Add an empty `RecordWin` method to `InMemoryPlayerStore` to satisfy the interface.

## Exercise 30

Call `RecordWin` in `processWin` with a hard-coded name "Bob".

## Exercise 31

Update the test to verify the correct player name is passed to `RecordWin`.

## Exercise 32

Update `processWin` to accept `http.Request` and extract the player name from URL.

## Exercise 33

DRY up by extracting player name once in `ServeHTTP` and passing it to both methods.

## Exercise 34

Create `server_integration_test.go` that tests `PlayerServer` with `InMemoryPlayerStore` - POST 3 wins then GET score.

## Exercise 35

Create `in_memory_player_store.go` with a working `InMemoryPlayerStore` that uses a map and a constructor.

## Exercise 36

Update `main.go` to use the constructor function.
