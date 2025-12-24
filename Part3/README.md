# project_part3

ALSO CHANGE THE FOLLOWING IN PART 1 POF THE PROJECT WHICH WE WILL UPLOAD IN GITHUB!!!!!
IMPORTANT CHANGE!!!!!!!!!!!!!!!

changes in ivfpq c source code, in ivfpq_init about 
    // index->k = k_clusters; line 335

    and change it into:
    
    if(ivf_temp->k <= 0)
    {
        fprintf(stderr, "Error in kclusters\n");
        exit(1);
    }
    
    index->k = ivf_temp->k;
    k_clusters = index->k;

    lines 351 - 358