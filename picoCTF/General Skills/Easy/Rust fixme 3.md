# PicoCTF - Rust fixme 3

## Challenge Overview
**Title:** Rust fixme 3  
**Category:** General Skills  
**Difficulty:** Easy  
**Files Provided:** fixme3.tar.gz

## Description
Have you heard of Rust? Fix the syntax errors in this Rust file to print the flag! Download the Rust code here.  

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
   Compiling rust_proj v0.1.0 (/home/george/Downloads/fixme3)
error[E0133]: call to unsafe function `std::slice::from_raw_parts` is unsafe and requires unsafe function or block
  --> src/main.rs:31:31
   |
31 |         let decrypted_slice = std::slice::from_raw_parts(decrypted_ptr, decrypted_len);
   |                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ call to unsafe function
   |
   = note: consult the function's documentation for information on how to avoid undefined behavior

For more information about this error, try `rustc --explain E0133`.
error: could not compile `rust_proj` (bin "rust_proj") due to 1 previous error

```
The **error** has to do to calling an **unsafe** function in a safe context.

### Source Code
```rust
use xor_cryptor::XORCryptor;

fn decrypt(encrypted_buffer: Vec<u8>, borrowed_string: &mut String) {
    // Key for decryption
    let key = String::from("CSUCKS");

    // Editing our borrowed value
    borrowed_string.push_str("PARTY FOUL! Here is your flag: ");

    // Create decryption object
    let res = XORCryptor::new(&key);
    if res.is_err() {
        return;
    }
    let xrc = res.unwrap();

    // Did you know you have to do "unsafe operations in Rust?
    // https://doc.rust-lang.org/book/ch19-01-unsafe-rust.html
    // Even though we have these memory safe languages, sometimes we need to do things outside of the rules
    // This is where unsafe rust comes in, something that is important to know about in order to keep things in perspective
    
    // unsafe {
        // Decrypt the flag operations 
        let decrypted_buffer = xrc.decrypt_vec(encrypted_buffer);

        // Creating a pointer 
        let decrypted_ptr = decrypted_buffer.as_ptr();
        let decrypted_len = decrypted_buffer.len();
        
        // Unsafe operation: calling an unsafe function that dereferences a raw pointer
        let decrypted_slice = std::slice::from_raw_parts(decrypted_ptr, decrypted_len);

        borrowed_string.push_str(&String::from_utf8_lossy(decrypted_slice));
    // }
    println!("{}", borrowed_string);
}

fn main() {
    // Encrypted flag values
    let hex_values = ["41", "30", "20", "63", "4a", "45", "54", "76", "12", "90", "7e", "53", "63", "e1", "01", "35", "7e", "59", "60", "f6", "03", "86", "7f", "56", "41", "29", "30", "6f", "08", "c3", "61", "f9", "35"];

    // Convert the hexadecimal strings to bytes and collect them into a vector
    let encrypted_buffer: Vec<u8> = hex_values.iter()
        .map(|&hex| u8::from_str_radix(hex, 16).unwrap())
        .collect();

    let mut party_foul = String::from("Using memory unsafe languages is a: ");
    decrypt(encrypted_buffer, &mut party_foul);
}
```

We open `main.rs` and find each line with an **error** indicated by the **compiler**.  
Each line has a **comment** next to it **indicating** what is wrong.

#### Error
```rust
// Did you know you have to do "unsafe operations in Rust?
// https://doc.rust-lang.org/book/ch19-01-unsafe-rust.html
// Even though we have these memory safe languages, sometimes we need to do things outside of the rules
// This is where unsafe rust comes in, something that is important to know about in order to keep things in perspective

// unsafe {
  // Decrypt the flag operations 
  let decrypted_buffer = xrc.decrypt_vec(encrypted_buffer);

  // Creating a pointer 
  let decrypted_ptr = decrypted_buffer.as_ptr();
  let decrypted_len = decrypted_buffer.len();

  // Unsafe operation: calling an unsafe function that dereferences a raw pointer
  let decrypted_slice = std::slice::from_raw_parts(decrypted_ptr, decrypted_len);

  borrowed_string.push_str(&String::from_utf8_lossy(decrypted_slice));
// }
```
The function `std::slice::from_raw_parts` is an **unsafe** function.  
**Unsafe** means that Rust's compiler **cannot** verify that the **pointer** will point to a **valid** memory location.  
This is because it is **accessing** a **raw pointer** in order to perform a **slice**.  

We see the **block** being **wrapped** by a commented out unsafe block
```rust
unsafe {
  ...
}
```
**Unsafe blocks** tell the Rust **compiler** to **trust** the developer and **not** perform memory **safety checks**.  
#### Fix
```rust
unsafe {
  // Decrypt the flag operations 
  let decrypted_buffer = xrc.decrypt_vec(encrypted_buffer);

  // Creating a pointer 
  let decrypted_ptr = decrypted_buffer.as_ptr();
  let decrypted_len = decrypted_buffer.len();
  
  // Unsafe operation: calling an unsafe function that dereferences a raw pointer
  let decrypted_slice = std::slice::from_raw_parts(decrypted_ptr, decrypted_len);

  borrowed_string.push_str(&String::from_utf8_lossy(decrypted_slice));
}
```
We have to simply **uncomment** this block.

## Solution

**Uncomment** the **unsafe** block in `decrypt()` like shown above and **run** the project using `cargo run`.