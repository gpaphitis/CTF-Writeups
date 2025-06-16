# PicoCTF - Rust fixme 2

## Challenge Overview
**Title:** Rust fixme 2  
**Category:** General Skills  
**Difficulty:** Easy  
**Files Provided:** fixme2.tar.gz

## Description
The Rust saga continues? I ask you, can I borrow that, pleeeeeaaaasseeeee? Download the Rust code here. 

## Analysis
Upon extracting the files from the tarball, we find a **Rust** project with a `main.rs` .  
When we run `cargo run` we are presented with some errors
```
$ cargo run       
   Compiling crossbeam-utils v0.8.20
   Compiling either v1.13.0
   Compiling crossbeam-epoch v0.9.18
   Compiling crossbeam-deque v0.8.5
   Compiling rayon-core v1.12.1
   Compiling rayon v1.10.0
   Compiling xor_cryptor v1.2.3
   Compiling rust_proj v0.1.0 (/home/george/Downloads/fixme2)
error[E0596]: cannot borrow `*borrowed_string` as mutable, as it is behind a `&` reference
 --> src/main.rs:9:5
  |
9 |     borrowed_string.push_str("PARTY FOUL! Here is your flag: ");
  |     ^^^^^^^^^^^^^^^ `borrowed_string` is a `&` reference, so the data it refers to cannot be borrowed as mutable
  |
help: consider changing this to be a mutable reference
  |
3 | fn decrypt(encrypted_buffer:Vec<u8>, borrowed_string: &mut String){ // How do we pass values to a function that we want to change?
  |                                                        +++

error[E0596]: cannot borrow `*borrowed_string` as mutable, as it is behind a `&` reference
  --> src/main.rs:20:5
   |
20 |     borrowed_string.push_str(&String::from_utf8_lossy(&decrypted_buffer));
   |     ^^^^^^^^^^^^^^^ `borrowed_string` is a `&` reference, so the data it refers to cannot be borrowed as mutable
   |
help: consider changing this to be a mutable reference
   |
3  | fn decrypt(encrypted_buffer:Vec<u8>, borrowed_string: &mut String){ // How do we pass values to a function that we want to change?
   |                                                        +++

For more information about this error, try `rustc --explain E0596`.
error: could not compile `rust_proj` (bin "rust_proj") due to 2 previous errors
```
The **errors** seem to refer to **borrowing** violations.

### Source Code
```rust
use xor_cryptor::XORCryptor;

fn decrypt(encrypted_buffer:Vec<u8>, borrowed_string: &String){ // How do we pass values to a function that we want to change?

    // Key for decryption
    let key = String::from("CSUCKS");

    // Editing our borrowed value
    borrowed_string.push_str("PARTY FOUL! Here is your flag: ");

    // Create decrpytion object
    let res = XORCryptor::new(&key);
    if res.is_err() {
        return; // How do we return in rust?
    }
    let xrc = res.unwrap();

    // Decrypt flag and print it out
    let decrypted_buffer = xrc.decrypt_vec(encrypted_buffer);
    borrowed_string.push_str(&String::from_utf8_lossy(&decrypted_buffer));
    println!("{}", borrowed_string);
}


fn main() {
    // Encrypted flag values
    let hex_values = ["41", "30", "20", "63", "4a", "45", "54", "76", "01", "1c", "7e", "59", "63", "e1", "61", "25", "0d", "c4", "60", "f2", "12", "a0", "18", "03", "51", "03", "36", "05", "0e", "f9", "42", "5b"];

    // Convert the hexadecimal strings to bytes and collect them into a vector
    let encrypted_buffer: Vec<u8> = hex_values.iter()
        .map(|&hex| u8::from_str_radix(hex, 16).unwrap())
        .collect();

    let party_foul = String::from("Using memory unsafe languages is a: "); // Is this variable changeable?
    decrypt(encrypted_buffer, &party_foul); // Is this the correct way to pass a value to a function so that it can be changed?
}
```

We open `main.rs` and find each line with an **error** indicated by the **compiler**.  
Each line has a **comment** next to it **indicating** what is wrong.

#### First Error
```rust
fn decrypt(encrypted_buffer:Vec<u8>, borrowed_string: &String){ // How do we pass values to a function that we want to change?

    // Key for decryption
    let key = String::from("CSUCKS");

    // Editing our borrowed value
    borrowed_string.push_str("PARTY FOUL! Here is your flag: ");
```
`borrowed_string` is an **immutable** reference.  
Trying to **execute**
```rust
borrowed_string.push_str("PARTY FOUL! Here is your flag: ");
```
Will try to create a **mutable** reference.  
This is illegal because there cannot exist a **mutable** and an **immutable** reference.
#### Fix
```rust
fn decrypt(encrypted_buffer:Vec<u8>, borrowed_string: &mut String){ 
```
We simply **change** the argument `borrowed_string` to be a **mutable** reference.

#### Second Error
```rust
let party_foul = String::from("Using memory unsafe languages is a: "); // Is this variable changeable?
decrypt(encrypted_buffer, &party_foul); // Is this the correct way to pass a value to a function so that it can be changed?
```
`part_foul` is an **immutable** variable.  
`decrypt()` expects a **mutable** reference fpr the **second** argument.  
#### Fix
```rust
let mut party_foul = String::from("Using memory unsafe languages is a: "); // Is this variable changeable?
decrypt(encrypted_buffer, &mut party_foul); // Is this the correct way to pass a value to a function so that it can be changed?
```
We have to change `party_foul` to be a **mutable** variable and change the argument we pass to `decrypt()` to a **mutable** .reference
## Solution

**Fix** the code **following** the above **two** fixes and **run** the project using `cargo run`.