# PicoCTF - Rust fixme 1

## Challenge Overview
**Title:** Rust fixme 1  
**Category:** General Skills  
**Difficulty:** Easy  
**Files Provided:** fixme1.tar.gz

## Description
Have you heard of Rust? Fix the syntax errors in this Rust file to print the flag! Download the Rust code here. 

## Analysis
Upon extracting the files from the tarball, we find a **Rust** project with a `main.rs` .  
When we run `cargo run` we are presented with some errors
```
$ cargo run       
   Compiling crossbeam-utils v0.8.20
   Compiling rayon-core v1.12.1
   Compiling either v1.13.0
   Compiling crossbeam-epoch v0.9.18
   Compiling crossbeam-deque v0.8.5
   Compiling rayon v1.10.0
   Compiling xor_cryptor v1.2.3
   Compiling rust_proj v0.1.0 (/home/george/Downloads/fixme1)
error: expected `;`, found keyword `let`
 --> src/main.rs:5:37
  |
5 |     let key = String::from("CSUCKS") // How do we end statements in Rust?
  |                                     ^ help: add `;` here
...
8 |     let hex_values = ["41", "30", "20", "63", "4a", "45", "54", "76", "01", "1c", "7e", "59", "63", "e1",...
  |     --- unexpected token

error: argument never used
  --> src/main.rs:26:9
   |
25 |         ":?", // How do we print out a variable in the println function? 
   |         ---- formatting specifier missing
26 |         String::from_utf8_lossy(&decrypted_buffer)
   |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ argument never used

error[E0425]: cannot find value `ret` in this scope
  --> src/main.rs:18:9
   |
18 |         ret; // How do we return in rust?
   |         ^^^ help: a local variable with a similar name exists: `res`

For more information about this error, try `rustc --explain E0425`.
error: could not compile `rust_proj` (bin "rust_proj") due to 3 previous errors
```

### Source Code
```rust
use xor_cryptor::XORCryptor;

fn main() {
    // Key for decryption
    let key = String::from("CSUCKS") // How do we end statements in Rust?

    // Encrypted flag values
    let hex_values = ["41", "30", "20", "63", "4a", "45", "54", "76", "01", "1c", "7e", "59", "63", "e1", "61", "25", "7f", "5a", "60", "50", "11", "38", "1f", "3a", "60", "e9", "62", "20", "0c", "e6", "50", "d3", "35"];

    // Convert the hexadecimal strings to bytes and collect them into a vector
    let encrypted_buffer: Vec<u8> = hex_values.iter()
        .map(|&hex| u8::from_str_radix(hex, 16).unwrap())
        .collect();

    // Create decrpytion object
    let res = XORCryptor::new(&key);
    if res.is_err() {
        ret; // How do we return in rust?
    }
    let xrc = res.unwrap();

    // Decrypt flag and print it out
    let decrypted_buffer = xrc.decrypt_vec(encrypted_buffer);
    println!(
        ":?", // How do we print out a variable in the println function? 
        String::from_utf8_lossy(&decrypted_buffer)
    );
}
```

We open `main.rs` and find each line with an **error** indicated by the **compiler**.  
Each line has a **comment** next to it **indicating** what is wrong.

#### First Error
```rust
let key = String::from("CSUCKS") // How do we end statements in Rust?
```
In Rust, all **statements** are **terminated** with a `;`.
#### Fix
```rust
let key = String::from("CSUCKS"); // How do we end statements in Rust?
```

#### Second Error
```rust
if res.is_err() {
   ret; // How do we return in rust?
}
```
`return` is the correct **keyword** to return.
#### Fix
```rust
if res.is_err() {
   return; // How do we return in rust?
}
```

#### Third Error
```rust
println!(
        ":?", // How do we print out a variable in the println function? 
        String::from_utf8_lossy(&decrypted_buffer)
    );
```
To **embed** a variable in the `println!` macro, we use `{}` inside the **string** format.
#### Fix
```rust
println!(
   "{}", // How do we print out a variable in the println function? 
   String::from_utf8_lossy(&decrypted_buffer)
);
```
Now we can **run** the project using `cargo run` and get the **flag**.
## Solution

**Fix** the code **following** the above **three** fixes and **run** the project using `cargo run`.