#ifndef UTILS_H
#define UTILS_H

// Given numbers a and b, returns a random float in [a,b)
float uniform_distribution(void* a, void* b);

// Returns a random float from a Gaussian distribution with mean 0 and variance 1
float gaussian_distribution(void);

// Generates a random vector of dimension d with Gaussian distributed components
void generate_random_vector(float* v, int d);

// Normalizes a float vector to unit L2 norm; if zero vector, sets v[0]=1 and others 0
void normalize_vector(float* v, int d);

// computes the dot product of two vectors of dimension d of given data type for b
static inline float dot_product(const float* a, const void* b, int d, DataType data_typeb)
{
    float sum = 0.0;
    for(int i = 0; i < d; i++)
    {
        if (data_typeb == DATA_TYPE_FLOAT)
            sum += a[i] * ((const float*)b)[i];
        else
            sum += a[i] * (float)((const uint8_t*)b)[i];
    }

    return sum;
}

// Computes the Euclidean distance between two vectors a and b of given data types
static inline double euclidean_distance(const void* a, const void* b, const int dimension, DataType data_typea , DataType data_typeb)
{
    const float* fa = (const float*)a;
    const float* fb = (const float*)b;
    const uint8_t* ua = (const uint8_t*)a;
    const uint8_t* ub = (const uint8_t*)b;

    double sum = 0.0;
    double diff = 0.0;
    for(int i = 0; i < dimension; i++)
    {
        if (data_typea == DATA_TYPE_FLOAT && data_typeb == DATA_TYPE_FLOAT)
            diff = fa[i] - fb[i];
        else if (data_typea == DATA_TYPE_FLOAT && data_typeb == DATA_TYPE_UINT8)
            diff = fa[i] - (double)ub[i];
        else if (data_typea == DATA_TYPE_UINT8 && data_typeb == DATA_TYPE_FLOAT)
            diff = (double)ua[i] - fb[i];
        else
            diff = (double)ua[i] - (double)ub[i];
        sum += diff * diff;
    }
    
    return sqrt(sum);
}

// Computes the norm between two vectors a and b of given data types
static inline double norm(const void* a, const void* b, const int dimension, DataType data_typea , DataType data_typeb)
{
    const float* fa = (const float*)a;
    const float* fb = (const float*)b;
    const uint8_t* ua = (const uint8_t*)a;
    const uint8_t* ub = (const uint8_t*)b;

    double sum = 0.0;
    double diff = 0.0;
    for(int i = 0; i < dimension; i++)
    {
        if (data_typea == DATA_TYPE_FLOAT && data_typeb == DATA_TYPE_FLOAT)
            diff = fa[i] - fb[i];
        else if (data_typea == DATA_TYPE_FLOAT && data_typeb == DATA_TYPE_UINT8)
            diff = fa[i] - (double)ub[i];
        else if (data_typea == DATA_TYPE_UINT8 && data_typeb == DATA_TYPE_FLOAT)
            diff = (double)ua[i] - fb[i];
        else
            diff = (double)ua[i] - (double)ub[i];
        sum += diff * diff;
    }

    return sum;
}

// Computes the Hamming distance between two binary vectors a and b of dimension d
int hamming_distance(const int* a, const int* b, int d);

// Returns the first 'probes' neighbors from point 'a' sorted by hamming distance
void get_hamming_neighbors(uint64_t bucket, int probes, int kproj, uint64_t* neighbors);

// Computes cosine distance = 1 - cos(a,b) for generic input types
static inline double cosine_distance(const void* a, const void* b, int d, DataType data_typea, DataType data_typeb)
{
    double dot = 0.0;
    double na = 0.0;
    double nb = 0.0;

    const float* fa = (const float*)a;
    const float* fb = (const float*)b;
    const uint8_t* ua = (const uint8_t*)a;
    const uint8_t* ub = (const uint8_t*)b;

    for (int i = 0; i < d; i++)
    {
        double va = (data_typea == DATA_TYPE_FLOAT) ? (double)fa[i] : (double)ua[i];
        double vb = (data_typeb == DATA_TYPE_FLOAT) ? (double)fb[i] : (double)ub[i];
        dot += va * vb;
        na += va * va;
        nb += vb * vb;
    }

    if (na == 0.0 || nb == 0.0)
        return 1.0; // if any vector is zero, define distance as max

    double sim = dot / (sqrt(na) * sqrt(nb));
    // Clamp numerical errors
    if (sim > 1.0) sim = 1.0;
    if (sim < -1.0) sim = -1.0;
    return 1.0 - sim;
}

#endif
