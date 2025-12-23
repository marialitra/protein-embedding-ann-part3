emb:
	python3 src/protein_embed.py \
	-i Data/subset_1k.fasta \
	-o output/vectors.dat \
	-model esm2_t6_8M_UR50D

emb_50k:
	python3 src/protein_embed_danai.py \
	-i Data/swissprot_50k.fasta \
	-o output/vectors_50k_opt.dat \
	--batch-size 64 \
	-model esm2_t6_8M_UR50D

search:
	python src/protein_search.py \
	-d output/vectors.dat -q Data/targets.fasta \
	-o output/results.txt \
	-method ivfflat

# Possible Inputs:
# -method <all|lsh|hypercube|ivfflat|ivfpq>