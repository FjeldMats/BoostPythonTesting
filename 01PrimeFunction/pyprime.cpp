#include <iostream>
#include <string>
#include <boost/python.hpp>
#include <boost/python/str.hpp>
#include <boost/python/extract.hpp>
#include <bitset>
#include <cmath>
#include <vector>
#include <fstream>

std::vector<long> simpleSieve(long limit, std::vector<long> &prime)
{
    std::vector<bool> mark(limit + 1, true);
    for (long p = 2; p * p <= limit; ++p)
    {
        if (mark[p] == true)
        {
            for (long i = p * p; i <= limit; i += p)
                mark[i] = false;
        }
    }

    for (long p = 2; p <= limit; ++p)
    {
        if (mark[p] == true)
        {
            prime.push_back(p);
        }
    }
    return prime;
}

boost::python::list segmentedSieve(boost::python::long_ py_num)
{
    long n = boost::python::extract<long>(py_num);
    long limit = floor(sqrt(n)) + 1;
    std::vector<long> prime;
    prime.reserve(limit); // Preallocate memory
    prime = simpleSieve(limit, prime);

    long low = limit;
    long high = 2 * limit;

    boost::python::list pyprimes;

    for (auto &p : prime)
    {
        pyprimes.append(p);
    }

    while (low < n)
    {
        if (high >= n)
            high = n;

        std::vector<unsigned int> mark((limit + 1) / 32 + 1, ~0); // Use a custom bitset

        for (long i = 0; i < prime.size(); ++i)
        {
            long loLim = prime[i] * ((low + prime[i] - 1) / prime[i]); // Avoid unnecessary division and multiplication

            if (loLim < low)
                loLim += prime[i];

            if (!(loLim & 1)) // Make sure loLim is odd
                loLim += prime[i];

            for (long j = loLim; j < high; j += prime[i] * 2) // Increment by 2*p to avoid even numbers
                mark[(j - low) / 32] &= ~(1 << ((j - low) & 31));
        }

        if (low == limit) // Check the number 2
            pyprimes.append(2);

        for (long i = low | 1; i < high; i += 2) // Skip even numbers
            if (mark[(i - low) / 32] & (1 << ((i - low) & 31)))
                pyprimes.append(i);

        low = low + limit;
        high = high + limit;
    }

    // Open a file to write the prime numbers
    std::ofstream file("primes.txt");

    // Check if the file is open
    if (!file.is_open())
    {
        throw std::runtime_error("Unable to open file");
    }

    // Write the prime numbers to the file
    for (int i = 0; i < len(pyprimes); ++i)
    {
        file << boost::python::extract<long>(pyprimes[i]) << "\n";
    }

    // Close the file
    file.close();

    return pyprimes;
}

BOOST_PYTHON_MODULE(pyprime)
{
    using namespace boost::python;
    def("primes", segmentedSieve);
}