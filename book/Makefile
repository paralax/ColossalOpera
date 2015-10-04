EASYFILES=../easy/ZZ_approximate_pi.md
EASYFILES+=../easy/ZZ_balancing_words.md
EASYFILES+=../easy/ZZ_cellular_automata.md
\ASYFILES+=../easy/ZZ_happy_numbers.md
EASYFILES+=../easy/ZZ_letters_in_order.md
EASYFILES+=../easy/ZZ_palindromic_numbers.md
EASYFILES+=../easy/ZZ_pronouncing_hex.md
EASYFILES+=../easy/ZZ_shuffle.md
EASYFILES+=../easy/ZZ_thue_morse.md
EASYFILES+=../easy/ZZ_vampire_numbers.md
EASYFILES+=../easy/abundance_and_deficiency.md
EASYFILES+=../easy/alliteration.md
EASYFILES+=../easy/anagram_detector.md
EASYFILES+=../easy/baum_sweet.md
EASYFILES+=../easy/broken_keyboard.md
EASYFILES+=../easy/capwords.md
EASYFILES+=../easy/collatz_conjecture.md
EASYFILES+=../easy/concatenated_ints.md
EASYFILES+=../easy/condensing_sentences.md
EASYFILES+=../easy/double_knot.md
EASYFILES+=../easy/fresh_eggs.md
EASYFILES+=../easy/graph_degree.md
EASYFILES+=../easy/harshad_number.md
EASYFILES+=../easy/integer_sequence_search_1.md
EASYFILES+=../easy/jolly_jumper.md
EASYFILES+=../easy/l33tspeak.md
EASYFILES+=../easy/most_presidents_alive.md
EASYFILES+=../easy/pandigital_roman_numbers.md
EASYFILES+=../easy/pell_number.md
EASYFILES+=../easy/perfect_numbers.md
EASYFILES+=../easy/primes_in_grids.md
EASYFILES+=../easy/random_name_generator.md
EASYFILES+=../easy/roller_coaster_words.md
EASYFILES+=../easy/ruth_aaron_pairs.md
EASYFILES+=../easy/safe_primes.md
EASYFILES+=../easy/stock_market.md
EASYFILES+=../easy/sub-words.md
EASYFILES+=../easy/typo_maker.md
EASYFILES+=../easy/wedderburn-etherington_sequence.md
EASYFILES+=../easy/xor_multiplication.md

INTFILES=../intermediate/ZZ_closest_pair_of_points.md
INTFILES+=../intermediate/ZZ_connect_four.md
INTFILES+=../intermediate/ZZ_detect_four_sided_figures.md
INTFILES+=../intermediate/ZZ_dna_restriction_enzymes.md
INTFILES+=../intermediate/ZZ_field_irrigation.md
INTFILES+=../intermediate/ZZ_packing_box_sentence.md
INTFILES+=../intermediate/ZZ_polyminos.md
INTFILES+=../intermediate/ZZ_set_solver.md
INTFILES+=../intermediate/ZZ_spellcheck.md
INTFILES+=../intermediate/ZZ_stream_cipher.md
INTFILES+=../intermediate/ZZ_web_api.md
INTFILES+=../intermediate/anagram_maker.md
INTFILES+=../intermediate/ancestors.md
INTFILES+=../intermediate/brick_walls.md
INTFILES+=../intermediate/calkin_wilf.md
INTFILES+=../intermediate/change_ringing.md
INTFILES+=../intermediate/cribbage_scoring.md
INTFILES+=../intermediate/cyclic_numbers.md
INTFILES+=../intermediate/cyclic_words.md
INTFILES+=../intermediate/de_bruijn.md
INTFILES+=../intermediate/digit_tower.md
INTFILES+=../intermediate/equation_snake.md
INTFILES+=../intermediate/friedman_numbers.md
INTFILES+=../intermediate/graph_radius.md
INTFILES+=../intermediate/hitori_solver.md
INTFILES+=../intermediate/ipv4_subnet_calculator.md
INTFILES+=../intermediate/isomorphic_words.md
INTFILES+=../intermediate/laser_box.md
INTFILES+=../intermediate/longest_common_substring.md
INTFILES+=../intermediate/magic_squares.md
INTFILES+=../intermediate/mathagrams.md
INTFILES+=../intermediate/packing_stacks_of_boxes.md
INTFILES+=../intermediate/picture_taking.md
INTFILES+=../intermediate/polite_numbers.md
INTFILES+=../intermediate/polydivisible_numbers.md
INTFILES+=../intermediate/prime_in_bases.md
INTFILES+=../intermediate/punch_card.md
INTFILES+=../intermediate/reversi_moves.md
INTFILES+=../intermediate/singles.md
INTFILES+=../intermediate/slitherlink.md
INTFILES+=../intermediate/spinning_gears.md
INTFILES+=../intermediate/spoonerism.md
INTFILES+=../intermediate/syllablizer.md
INTFILES+=../intermediate/tile_shuffling.md
INTFILES+=../intermediate/trees_and_parks.md
INTFILES+=../intermediate/two_for_one.md
INTFILES+=../intermediate/ulam_number.md
INTFILES+=../intermediate/unique_county_names.md
INTFILES+=../intermediate/vaki_puzzle_solver.md
INTFILES+=../intermediate/word_in_a_box.md
INTFILES+=../intermediate/word_stacks.md
INTFILES+=../intermediate/word_wheel.md
INTFILES+=../intermediate/xor_decoding.md
INTFILES+=../intermediate/zeckendorf_representation.md
INTFILES+=../intermediate/zombie_village_graph_partition.md

HARDFILES=../hard/8_puzzle.md
HARDFILES+=../hard/ZZ_coiled_sentence.md
HARDFILES+=../hard/ZZ_delivery_schedule.md
HARDFILES+=../hard/ZZ_elevator_scheduling.md
HARDFILES+=../hard/ZZ_golomb_rulers.md
HARDFILES+=../hard/ZZ_kakuro_solver.md
HARDFILES+=../hard/ZZ_kanoodle.md
HARDFILES+=../hard/ZZ_pile_of_paper.md
HARDFILES+=../hard/ZZ_protein_secondary_structure.md
HARDFILES+=../hard/ZZ_sequence_alignment.md
HARDFILES+=../hard/ZZ_shortest_splitlines.md
HARDFILES+=../hard/ZZ_stable_marriage.md
HARDFILES+=../hard/ZZ_stepstring_discrepency.md
HARDFILES+=../hard/anomaly_detection.md
HARDFILES+=../hard/chess_solitaire.md
HARDFILES+=../hard/congreunt_numbers.md
HARDFILES+=../hard/dna_shotgun_sequencing.md
HARDFILES+=../hard/friends.md
HARDFILES+=../hard/going_home.md
HARDFILES+=../hard/grocery_shopping.md
HARDFILES+=../hard/integer_sequence_search_2.md
HARDFILES+=../hard/microgrid_edges.txt
HARDFILES+=../hard/microgrid_power.md
HARDFILES+=../hard/museum_cameras_1.md
HARDFILES+=../hard/museum_cameras_2.md
HARDFILES+=../hard/paired_music.md
HARDFILES+=../hard/street_sweepers.md
HARDFILES+=../hard/text_summarizer.md

PANDOCARGS=--variable sansfont=Arial --latex-engine=xelatex -f markdown -t latex

pdf: book.pdf

book.pdf: book.tex easy.tex int.tex hard.tex
	pdflatex -shell-escape book.tex
	# do this thrice because of the TOC and tables
	pdflatex -shell-escape book.tex
	pdflatex -shell-escape book.tex	

easy.tex: easy.md 
	pandoc easy.md -o easytmp.tex $(PANDOCARGS)
	cat easytmp.tex | python process.py > easy.tex
	
int.tex: int.md 
	pandoc int.md -o inttmp.tex $(PANDOCARGS)
	cat inttmp.tex | python process.py > int.tex
	
hard.tex: hard.md
	pandoc hard.md -o hardtmp.tex $(PANDOCARGS)
	cat hardtmp.tex | python process.py > hard.tex

easy.md:
	@echo $(EASYFILES)
	$(foreach f,$(EASYFILES), cat $(f) | sed "s/^# /## /g" | sed "s/^## Title/# Title/g" >> easy.md; echo "" >> easy.md;)

int.md:
	@echo $(INTFILES)
	$(foreach f,$(INTFILES), cat $(f) | sed "s/^# /## /g" | sed "s/^## Title/# Title/g" >> int.md; echo "" >> int.md;)	
	
hard.md:
	@echo $(HARDFILES)	
	$(foreach f,$(HARDFILES), cat $(f) | sed "s/^# /## /g" | sed "s/^## Title/# Title/g" >> hard.md; echo "" >> hard.md;)		

clean:
	rm -f easytmp.tex inttmp.tex hardtmp.tex easy.tex int.tex hard.tex
	rm -rf _minted-book
	rm -f book.aux book.log book.out book.pdf book.toc easy.md hard.md int.md texput.log

# TODO
# - fonts
