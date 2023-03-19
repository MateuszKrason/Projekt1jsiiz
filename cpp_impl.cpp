#include <chrono>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

// custom hexadecimal conversion function
std::string custom_hex(int num) {
  if (num < 0) {
    throw std::invalid_argument("hex() argument cannot be negative");
  }
  const std::string hex_digits = "0123456789abcdef";
  std::string result;
  while (num > 0) {
    int digit = num % 16;
    result = hex_digits[digit] + result;
    num /= 16;
  }
  if (result.empty()) {
    result = "0";
  }
  return "0x" + result;
}

int main() {
  int num_files = 10;  // specify the number of files to read
  std::string file_prefix = "data_";  // specify the file prefix

  for (int i = 1; i <= num_files; ++i) {
    // construct the filename
    std::string filename = file_prefix + std::to_string(i)+".txt";
    // read the number from the file
    std::ifstream file(filename);
    int num;
    file >> num;

    // perform the custom hexadecimal conversion
    auto start = std::chrono::high_resolution_clock::now();
    std::string hex_str = custom_hex(num);
    auto end = std::chrono::high_resolution_clock::now();

    // print the result and timing information
    std::cout << "File " << i << ": " << num << " -> " << hex_str << std::endl;
    std::cout << "Time taken: " << std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count() << " nanoseconds" << std::endl;

    // write the result and timing information to a text file
    std::string output_filename = "cpp_" + std::to_string(i) + ".txt";
    std::ofstream output_file(output_filename);
    output_file << hex_str << std::endl;
    output_file.close();
  }

  return 0;
}
