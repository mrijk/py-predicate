window.BENCHMARK_DATA = {
  "lastUpdate": 1776369634840,
  "repoUrl": "https://github.com/mrijk/py-predicate",
  "entries": {
    "Benchmark": [
      {
        "commit": {
          "author": {
            "email": "maurits.rijk@surf.nl",
            "name": "Maurits Rijk"
          },
          "committer": {
            "email": "maurits.rijk@surf.nl",
            "name": "Maurits Rijk"
          },
          "distinct": true,
          "id": "576f7b70e28daa7219b5fb9ba6997a46cce055b2",
          "message": "Fix git checkout after creating benchmark-results branch\n\nUse the original HEAD SHA instead of 'git checkout -' which fails in CI.\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)",
          "timestamp": "2026-04-16T16:32:48+02:00",
          "tree_id": "e89da6f2ae3a0c03ca82f6d12d42791fc300ad93",
          "url": "https://github.com/mrijk/py-predicate/commit/576f7b70e28daa7219b5fb9ba6997a46cce055b2"
        },
        "date": 1776350034899,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 4346429.33773941,
            "unit": "iter/sec",
            "range": "stddev: 1.4351485844827087e-7",
            "extra": "mean: 230.07391177791533 nsec\nrounds: 198020"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 7023899.501631043,
            "unit": "iter/sec",
            "range": "stddev: 1.9818765746380196e-8",
            "extra": "mean: 142.37105752549377 nsec\nrounds: 191571"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1708460.4392986156,
            "unit": "iter/sec",
            "range": "stddev: 5.9411729003736414e-8",
            "extra": "mean: 585.3223036352753 nsec\nrounds: 81480"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1285664.7274243955,
            "unit": "iter/sec",
            "range": "stddev: 6.777997993180733e-8",
            "extra": "mean: 777.80775863963 nsec\nrounds: 63497"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4341628.548935059,
            "unit": "iter/sec",
            "range": "stddev: 3.5914606804504635e-8",
            "extra": "mean: 230.3283177565446 nsec\nrounds: 194932"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7593407.5888174735,
            "unit": "iter/sec",
            "range": "stddev: 1.4303632028742598e-8",
            "extra": "mean: 131.69318099987976 nsec\nrounds: 74879"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 113804.9824815235,
            "unit": "iter/sec",
            "range": "stddev: 9.575430514609756e-7",
            "extra": "mean: 8.786961503749207 usec\nrounds: 77436"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 64532.43529857327,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013378956217639047",
            "extra": "mean: 15.496083409424788 usec\nrounds: 48172"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 63253.73486269541,
            "unit": "iter/sec",
            "range": "stddev: 0.000001407134749562101",
            "extra": "mean: 15.809343150577517 usec\nrounds: 44106"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1790544.5978546264,
            "unit": "iter/sec",
            "range": "stddev: 2.564537867768539e-7",
            "extra": "mean: 558.4893005168194 nsec\nrounds: 152859"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1179554.8586928137,
            "unit": "iter/sec",
            "range": "stddev: 7.063351877915586e-8",
            "extra": "mean: 847.7774413207056 nsec\nrounds: 57694"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 425209.5313217621,
            "unit": "iter/sec",
            "range": "stddev: 5.302050064308267e-7",
            "extra": "mean: 2.3517817131039003 usec\nrounds: 49806"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 61065.55390846884,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017433268361929266",
            "extra": "mean: 16.3758442525372 usec\nrounds: 16790"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 61459.64249392774,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018687491414136541",
            "extra": "mean: 16.27083984581916 usec\nrounds: 27998"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1711.9202168685717,
            "unit": "iter/sec",
            "range": "stddev: 0.000015000584184099688",
            "extra": "mean: 584.1393717688494 usec\nrounds: 425"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 49406.34815008121,
            "unit": "iter/sec",
            "range": "stddev: 0.000002039821188380243",
            "extra": "mean: 20.24031399694446 usec\nrounds: 28220"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 368814.5623234806,
            "unit": "iter/sec",
            "range": "stddev: 7.030232389289586e-7",
            "extra": "mean: 2.711389685103914 usec\nrounds: 45021"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 7011.430073695483,
            "unit": "iter/sec",
            "range": "stddev: 0.000013524576240654856",
            "extra": "mean: 142.62425631992852 usec\nrounds: 5657"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 22788.81761566246,
            "unit": "iter/sec",
            "range": "stddev: 0.000060872087824696825",
            "extra": "mean: 43.88117088236788 usec\nrounds: 10715"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 249715.50287235095,
            "unit": "iter/sec",
            "range": "stddev: 8.326102435454861e-7",
            "extra": "mean: 4.004557140015363 usec\nrounds: 55329"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 263221.60986995726,
            "unit": "iter/sec",
            "range": "stddev: 7.25734842973877e-7",
            "extra": "mean: 3.7990801761832658 usec\nrounds: 101751"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 273161.4370427265,
            "unit": "iter/sec",
            "range": "stddev: 7.25758930737852e-7",
            "extra": "mean: 3.6608388461640184 usec\nrounds: 101338"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 159439.85903808143,
            "unit": "iter/sec",
            "range": "stddev: 9.379826030713491e-7",
            "extra": "mean: 6.271957376487362 usec\nrounds: 46993"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 52726.0260222443,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018115200413904444",
            "extra": "mean: 18.965965680366565 usec\nrounds: 20717"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 69378.20787592656,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016137134600755795",
            "extra": "mean: 14.413747927711874 usec\nrounds: 17130"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 66708.72659153276,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016196831311309164",
            "extra": "mean: 14.990542483641542 usec\nrounds: 28823"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 271971.09649402247,
            "unit": "iter/sec",
            "range": "stddev: 7.937910169179534e-7",
            "extra": "mean: 3.676861302142004 usec\nrounds: 92251"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 245477.06427038496,
            "unit": "iter/sec",
            "range": "stddev: 7.97055291169034e-7",
            "extra": "mean: 4.073700339264823 usec\nrounds: 92251"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 290312.09238748514,
            "unit": "iter/sec",
            "range": "stddev: 7.100866351650935e-7",
            "extra": "mean: 3.4445688837007893 usec\nrounds: 57931"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 335286.48422457953,
            "unit": "iter/sec",
            "range": "stddev: 6.398481042028768e-7",
            "extra": "mean: 2.982524041530365 usec\nrounds: 105297"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 54118.593345474736,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018317887364300393",
            "extra": "mean: 18.477937769304894 usec\nrounds: 7890"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 19604.707324062136,
            "unit": "iter/sec",
            "range": "stddev: 0.0000033564649133269933",
            "extra": "mean: 51.00815755472334 usec\nrounds: 12237"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 1182528.7445594633,
            "unit": "iter/sec",
            "range": "stddev: 7.29310966176888e-8",
            "extra": "mean: 845.6454057465959 nsec\nrounds: 56266"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 125606.1905523038,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010492138889277484",
            "extra": "mean: 7.961391039748068 usec\nrounds: 28749"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 32259.33517625704,
            "unit": "iter/sec",
            "range": "stddev: 0.0000024039478924973177",
            "extra": "mean: 30.99877894371496 usec\nrounds: 8197"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "maurits.rijk@surf.nl",
            "name": "Maurits Rijk"
          },
          "committer": {
            "email": "maurits.rijk@surf.nl",
            "name": "Maurits Rijk"
          },
          "distinct": true,
          "id": "5ac6176043ad4e78cbc9432d0bf3a1d3e5d884da",
          "message": "Revert benchmark storage to benchmark-results branch\n\nPR comments are the primary way to view results.\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)",
          "timestamp": "2026-04-16T17:43:44+02:00",
          "tree_id": "1c1c5adf9a50c5bb6e18f1614e705cd3418be98d",
          "url": "https://github.com/mrijk/py-predicate/commit/5ac6176043ad4e78cbc9432d0bf3a1d3e5d884da"
        },
        "date": 1776354283523,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 8865112.41134673,
            "unit": "iter/sec",
            "range": "stddev: 1.0476655826924963e-8",
            "extra": "mean: 112.80172812248487 nsec\nrounds: 197006"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 8031739.911185254,
            "unit": "iter/sec",
            "range": "stddev: 7.437279841152687e-9",
            "extra": "mean: 124.50602373308533 nsec\nrounds: 79215"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1840706.240536461,
            "unit": "iter/sec",
            "range": "stddev: 3.64744239810009e-8",
            "extra": "mean: 543.2697396128548 nsec\nrounds: 88905"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1244371.3467019696,
            "unit": "iter/sec",
            "range": "stddev: 4.31613417858986e-8",
            "extra": "mean: 803.6186325330928 nsec\nrounds: 60872"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4500886.303528608,
            "unit": "iter/sec",
            "range": "stddev: 2.091977781121024e-8",
            "extra": "mean: 222.17846276543784 nsec\nrounds: 198729"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 8419403.538722366,
            "unit": "iter/sec",
            "range": "stddev: 9.38635286972577e-9",
            "extra": "mean: 118.7732593408569 nsec\nrounds: 83704"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 130896.06618463538,
            "unit": "iter/sec",
            "range": "stddev: 6.742411975124325e-7",
            "extra": "mean: 7.639648991356626 usec\nrounds: 89183"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 74823.90138729649,
            "unit": "iter/sec",
            "range": "stddev: 8.550231098280354e-7",
            "extra": "mean: 13.364713433263704 usec\nrounds: 56130"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 72620.52719446638,
            "unit": "iter/sec",
            "range": "stddev: 9.157597535083594e-7",
            "extra": "mean: 13.770211242368934 usec\nrounds: 50061"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 2121389.096836553,
            "unit": "iter/sec",
            "range": "stddev: 5.978477877740328e-8",
            "extra": "mean: 471.38924278022114 nsec\nrounds: 189466"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1284740.5632777729,
            "unit": "iter/sec",
            "range": "stddev: 5.687947537715745e-8",
            "extra": "mean: 778.3672661885049 nsec\nrounds: 62744"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 453241.10398544674,
            "unit": "iter/sec",
            "range": "stddev: 2.868149155593241e-7",
            "extra": "mean: 2.206331224610443 usec\nrounds: 47898"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 60297.18188167809,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010233518623464664",
            "extra": "mean: 16.58452300411506 usec\nrounds: 18149"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 60407.16179663409,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011222702317508703",
            "extra": "mean: 16.55432849777955 usec\nrounds: 26195"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1723.130150011558,
            "unit": "iter/sec",
            "range": "stddev: 0.000013663342280673728",
            "extra": "mean: 580.3392158121616 usec\nrounds: 468"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 48330.61288048313,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016154050554514265",
            "extra": "mean: 20.690819759991495 usec\nrounds: 26093"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 397070.68865447585,
            "unit": "iter/sec",
            "range": "stddev: 3.3662136382074187e-7",
            "extra": "mean: 2.518443261044088 usec\nrounds: 29107"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 7500.883330399033,
            "unit": "iter/sec",
            "range": "stddev: 0.000011917225759935006",
            "extra": "mean: 133.3176315311122 usec\nrounds: 5512"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 23891.9177573798,
            "unit": "iter/sec",
            "range": "stddev: 0.00008315693139144466",
            "extra": "mean: 41.85515830729483 usec\nrounds: 11484"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 268582.8847897811,
            "unit": "iter/sec",
            "range": "stddev: 4.84886489354301e-7",
            "extra": "mean: 3.72324543606975 usec\nrounds: 54723"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 284619.1313237412,
            "unit": "iter/sec",
            "range": "stddev: 5.057490084740347e-7",
            "extra": "mean: 3.513467261842443 usec\nrounds: 68559"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 295061.53146906453,
            "unit": "iter/sec",
            "range": "stddev: 5.486772007748592e-7",
            "extra": "mean: 3.3891236008338956 usec\nrounds: 94967"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 176293.03549054425,
            "unit": "iter/sec",
            "range": "stddev: 7.072571139239232e-7",
            "extra": "mean: 5.672373824737033 usec\nrounds: 50521"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 59001.028972354536,
            "unit": "iter/sec",
            "range": "stddev: 0.000002078599025940572",
            "extra": "mean: 16.94885695075859 usec\nrounds: 14862"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 76722.37487010902,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010446313748209742",
            "extra": "mean: 13.034007376505224 usec\nrounds: 16132"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 73378.20737817003,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011047507201038585",
            "extra": "mean: 13.62802439212353 usec\nrounds: 25336"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 289530.25219340133,
            "unit": "iter/sec",
            "range": "stddev: 4.048320041208551e-7",
            "extra": "mean: 3.4538705106781618 usec\nrounds: 86007"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 268088.47537228884,
            "unit": "iter/sec",
            "range": "stddev: 5.648037835058837e-7",
            "extra": "mean: 3.730111854347043 usec\nrounds: 92388"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 323330.8561517093,
            "unit": "iter/sec",
            "range": "stddev: 4.1863960398277626e-7",
            "extra": "mean: 3.092807200345866 usec\nrounds: 53496"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 355357.87716394395,
            "unit": "iter/sec",
            "range": "stddev: 4.824502216123831e-7",
            "extra": "mean: 2.814064536801167 usec\nrounds: 116755"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 60218.80693010738,
            "unit": "iter/sec",
            "range": "stddev: 0.00000116563701354853",
            "extra": "mean: 16.606107808821992 usec\nrounds: 10296"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 22316.814605648622,
            "unit": "iter/sec",
            "range": "stddev: 0.0000020143964235335685",
            "extra": "mean: 44.809262328454764 usec\nrounds: 12755"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 1322273.8116267845,
            "unit": "iter/sec",
            "range": "stddev: 4.6390979552473e-8",
            "extra": "mean: 756.2730133554614 nsec\nrounds: 65890"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 140612.00442118954,
            "unit": "iter/sec",
            "range": "stddev: 6.555051405943928e-7",
            "extra": "mean: 7.111768330992548 usec\nrounds: 30781"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 37031.769501468894,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015101355410568357",
            "extra": "mean: 27.003840579649705 usec\nrounds: 8418"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "maurits.rijk@gmail.com",
            "name": "Maurits",
            "username": "mrijk"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "419c86226cb75eeaa71bd625422ae6911170a7e0",
          "message": "Add compile_predicate: compile predicate trees to native callables (#10) (#211)\n\n* Add compile_predicate: compile predicate trees to native callables (#10)\n\nIntroduces compile_predicate(), try_compile_predicate(), NotCompilableError,\nand CompiledPredicate. Walks the predicate tree and builds a Python AST,\nthen calls compile() to produce a single native lambda — eliminating the\nchain of __call__ dispatches for supported predicate types.\n\nSupported types: all leaf comparisons (eq, ne, gt, ge, lt, le, in, not_in,\nis_none, is_not_none, is_truthy, is_falsy), all range predicates (ge_le,\nge_lt, gt_le, gt_lt), IsInstancePredicate (via delegation), and all boolean\ncombinators (and, or, not, xor) recursively.\n\nCompiledPredicate delegates repr, count, explain_failure, and __contains__\nto the wrapped predicate, so introspection is fully preserved.\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)\n\n* Refactor _to_ast to use singledispatch\n\nEach predicate type now has its own registered handler, mirroring the\npattern used by generate_true/generate_false. The circular import with\nis_none_predicate is resolved by importing compile_predicate after\nexception_predicate in __init__.py (suppressed via per-file I001 ignore).\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)\n\n* Add raw Python baseline to performance tests\n\nCompares interpreted and compiled predicates against equivalent plain\nPython lambdas to establish the theoretical performance ceiling.\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)\n\n* Remove predicate classes from __init__ public API\n\nCompiledPredicate, NotCompilableError, IntersectsPredicate, RaisesPredicate,\nPredicateError, and Spec must now be imported directly from their modules.\nUpdated affected tests accordingly.\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)\n\n* Add AllPredicate compilation support with performance benchmarks\n\nCompile all_p to a native generator expression (all(_p0(_e) for _e in x)),\nstoring the inner compiled fn directly to avoid double indirection.\nBenchmarks show ~1.69x speedup over interpreted for 100-element lists.\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)\n\n* Add AnyPredicate compilation support\n\nCompiles any_p to a native generator expression (any(_p0(_e) for _e in x)).\nRefactored AllPredicate handler to share _any_all_ast helper.\nBenchmarks show ~1.3x speedup over interpreted for 100-element lists.\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)\n\n* Add ListOfPredicate compilation support\n\nCompiles is_list_of_p to isinstance(x, list) and all(_p0(_e) for _e in x),\nreusing the _any_all_ast helper. Benchmarks show ~1.8x speedup over\ninterpreted for 100-element lists.\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)\n\n* Add ListOfPredicate optimizer\n\nOptimizes is_list_of_p with rules mirroring AllPredicate:\n- is_list_of_p(always_true_p) → is_list_p\n- is_list_of_p(always_false_p) → is_list_p & is_empty_p\n- is_list_of_p(~p) → is_list_p & ~any_p(p)  (De Morgan)\n- is_list_of_p(is_not_none_p) → is_list_p & ~any_p(is_none_p)\n- Propagates inner predicate optimization\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)\n\n* Compile always_true_p and always_false_p to constant expressions\n\nlambda x: True / lambda x: False — unblocks composed predicates\nthat previously raised NotCompilableError when containing these.\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)\n\n* Compile has_key_p and is_set_of_p\n\n- has_key_p(k): k in x  (key captured in namespace)\n- is_set_of_p(p): isinstance(x, set) and all(_p0(_e) for _e in x)\n\nExtracted _isinstance_and_all_ast helper shared by ListOfPredicate\nand SetOfPredicate handlers.\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)\n\n* Compile is_tuple_of_p to an inlined and-chain\n\nlen(x) == n and _p0(x[0]) and _p1(x[1]) and ...\n\nUnfolds the zip/all loop into direct subscript checks — no generator\noverhead, short-circuits on first failure. Each inner predicate is\ncompiled to its raw fn where possible.\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)\n\n* Compile named_p, is_close_p, and comp_p\n\n- named_p(name, v): constant True/False  (v fixed at construction time)\n- is_close_p(t, rel, abs): math.isclose(x, t, rel_tol=..., abs_tol=...)\n  stored in namespace, all tolerance args inlined as constants\n- comp_p(fn, p): _p0(_fn0(x))  — fn and compiled inner predicate stored\n  in namespace, inner compiled to raw fn where possible\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)\n\n* Refactor TupleOfPredicate compiler to use try_compile_predicate and list comprehension\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)\n\n* Extract _name() helper for ast.Name(id=..., ctx=ast.Load())\n\nReduces boilerplate across all AST node construction sites.\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)\n\n* Pass inner predicate to _any_all_ast to remove union type\n\nCallers now pass predicate.predicate directly, simplifying the\nsignature from AllPredicate | AnyPredicate to plain Predicate.\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)\n\n* Fix mypy error: pass inner predicate to _isinstance_and_all_ast\n\nSame refactor as _any_all_ast — callers now pass predicate.predicate\ndirectly, removing the invalid .predicate access on plain Predicate.\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)\n\n* Compile CountPredicate\n\nCompiles count_p(filter_p, length_p) to:\n  _length_p(sum(1 for _e in x if _filter_p(_e)))\n\nReplaces ilen() with sum(1 for ...) — no more_itertools dependency\nin the compiled form. Both filter and length predicates are compiled\nvia try_compile_predicate where possible.\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)\n\n* Compile HasLengthPredicate\n\nCompiles has_length_p(length_p) to _length_p(sum(1 for _ in x)),\nreplacing ilen() with a pure builtin. is_empty_p and is_not_empty_p\ncompile transitively.\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)\n\n* Add pull-requests: write permission to benchmark workflow\n\nRequired for benchmark-action to post PR comments.\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)\n\n* Raise benchmark alert threshold to 150%\n\n120% is too tight for GitHub Actions variable runner performance,\ncausing false positive alerts from CI noise.\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)\n\n---------\n\nCo-authored-by: Maurits Rijk <maurits.rijk@surf.nl>",
          "timestamp": "2026-04-16T21:46:17+02:00",
          "tree_id": "bf21c734e88bd282c6e78fc3830c0babe1c4b198",
          "url": "https://github.com/mrijk/py-predicate/commit/419c86226cb75eeaa71bd625422ae6911170a7e0"
        },
        "date": 1776368830290,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 7909345.292621452,
            "unit": "iter/sec",
            "range": "stddev: 3.7495811848638945e-8",
            "extra": "mean: 126.43271509879456 nsec\nrounds: 196851"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 7223171.044251501,
            "unit": "iter/sec",
            "range": "stddev: 2.1863097377826788e-8",
            "extra": "mean: 138.4433504168286 nsec\nrounds: 198020"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1703447.5042505125,
            "unit": "iter/sec",
            "range": "stddev: 5.516834149838379e-8",
            "extra": "mean: 587.0448003268423 nsec\nrounds: 82082"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1287519.3843979286,
            "unit": "iter/sec",
            "range": "stddev: 6.451011673346109e-8",
            "extra": "mean: 776.6873354435912 nsec\nrounds: 63658"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4416963.528205675,
            "unit": "iter/sec",
            "range": "stddev: 4.320788868650335e-8",
            "extra": "mean: 226.39987711336957 nsec\nrounds: 197668"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7650247.86988526,
            "unit": "iter/sec",
            "range": "stddev: 1.300377789264011e-8",
            "extra": "mean: 130.71471892256457 nsec\nrounds: 76723"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 116011.00702877427,
            "unit": "iter/sec",
            "range": "stddev: 9.941200793370846e-7",
            "extra": "mean: 8.61987173123986 usec\nrounds: 73611"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 64519.093736389535,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014214807599244266",
            "extra": "mean: 15.499287762561801 usec\nrounds: 48196"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 61659.679059311515,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015072116165528264",
            "extra": "mean: 16.218053925290185 usec\nrounds: 43004"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1747705.1757979174,
            "unit": "iter/sec",
            "range": "stddev: 2.488100736900479e-7",
            "extra": "mean: 572.1788856884563 nsec\nrounds: 165536"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1229654.5435936889,
            "unit": "iter/sec",
            "range": "stddev: 7.977728951508346e-8",
            "extra": "mean: 813.2365347729948 nsec\nrounds: 57396"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 424420.3758711412,
            "unit": "iter/sec",
            "range": "stddev: 5.312650729527314e-7",
            "extra": "mean: 2.35615455065619 usec\nrounds: 46729"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 61257.35283358938,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018583695419900869",
            "extra": "mean: 16.324570908517416 usec\nrounds: 18129"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 61232.40197544678,
            "unit": "iter/sec",
            "range": "stddev: 0.0000019786391960251025",
            "extra": "mean: 16.331222812408765 usec\nrounds: 28046"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1732.7609801874264,
            "unit": "iter/sec",
            "range": "stddev: 0.00002409145939843168",
            "extra": "mean: 577.1136420049312 usec\nrounds: 419"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 49213.5469371031,
            "unit": "iter/sec",
            "range": "stddev: 0.0000021721756254008225",
            "extra": "mean: 20.319608364705765 usec\nrounds: 26660"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 367893.03486986185,
            "unit": "iter/sec",
            "range": "stddev: 5.808631073026614e-7",
            "extra": "mean: 2.7181813875702736 usec\nrounds: 43895"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 7133.624122254545,
            "unit": "iter/sec",
            "range": "stddev: 0.000015707852518187718",
            "extra": "mean: 140.18120142892465 usec\nrounds: 4478"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 22704.34888011163,
            "unit": "iter/sec",
            "range": "stddev: 0.000057223061417126245",
            "extra": "mean: 44.044425377728935 usec\nrounds: 10198"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 233515.7401084321,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011937042441428687",
            "extra": "mean: 4.28236657424315 usec\nrounds: 50721"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 254807.9177024556,
            "unit": "iter/sec",
            "range": "stddev: 7.98750695380642e-7",
            "extra": "mean: 3.924524830377212 usec\nrounds: 93897"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 265626.59370178415,
            "unit": "iter/sec",
            "range": "stddev: 9.110145342945278e-7",
            "extra": "mean: 3.764683294936531 usec\nrounds: 100011"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 157975.71409905178,
            "unit": "iter/sec",
            "range": "stddev: 0.00000102243559371439",
            "extra": "mean: 6.330086910529764 usec\nrounds: 41537"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 52296.08282933874,
            "unit": "iter/sec",
            "range": "stddev: 0.0000026653692390580678",
            "extra": "mean: 19.121891084335438 usec\nrounds: 23229"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 68858.28221247352,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016584449122725396",
            "extra": "mean: 14.522581276633302 usec\nrounds: 17219"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 65661.27651833277,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018526922972728358",
            "extra": "mean: 15.22967650074238 usec\nrounds: 26371"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 263424.1419053021,
            "unit": "iter/sec",
            "range": "stddev: 7.41112892753627e-7",
            "extra": "mean: 3.7961592766979124 usec\nrounds: 87169"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 238608.2242360232,
            "unit": "iter/sec",
            "range": "stddev: 8.334452962748695e-7",
            "extra": "mean: 4.190970379171985 usec\nrounds: 85683"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 285363.83846138837,
            "unit": "iter/sec",
            "range": "stddev: 6.901861193586582e-7",
            "extra": "mean: 3.5042982509338048 usec\nrounds: 52315"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 329749.6064755293,
            "unit": "iter/sec",
            "range": "stddev: 7.142366855267026e-7",
            "extra": "mean: 3.0326040740073177 usec\nrounds: 96071"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 46930.193610195296,
            "unit": "iter/sec",
            "range": "stddev: 0.000005491277081919707",
            "extra": "mean: 21.308243650261783 usec\nrounds: 9095"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 18429.48500324957,
            "unit": "iter/sec",
            "range": "stddev: 0.000010009118350610304",
            "extra": "mean: 54.260875972588245 usec\nrounds: 10151"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 106253.98076505146,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012254270235162476",
            "extra": "mean: 9.411412097690697 usec\nrounds: 39578"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 122434.13311780914,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012059770279896299",
            "extra": "mean: 8.167656964073698 usec\nrounds: 18689"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 31835.946377539254,
            "unit": "iter/sec",
            "range": "stddev: 0.0000026977636668046",
            "extra": "mean: 31.41103418573149 usec\nrounds: 7781"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "maurits.rijk@surf.nl",
            "name": "Maurits Rijk"
          },
          "committer": {
            "email": "maurits.rijk@surf.nl",
            "name": "Maurits Rijk"
          },
          "distinct": true,
          "id": "54a780c2e950b45dc1c2149057ccc0e6ee9f4aa0",
          "message": "Improve README with comprehensive feature coverage\n\nExpands the README from a minimal two-example intro to a full feature\noverview: composition operators, built-in predicates by category,\nexplain, optimizer, compile_predicate, value generation, recursive\npredicates, runtime instrumentation (Spec), analysis, and serialization.\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)",
          "timestamp": "2026-04-16T21:59:30+02:00",
          "tree_id": "77dfac1605d49c2a70f23fbe48e8f8b80136f047",
          "url": "https://github.com/mrijk/py-predicate/commit/54a780c2e950b45dc1c2149057ccc0e6ee9f4aa0"
        },
        "date": 1776369634495,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 4378232.604992516,
            "unit": "iter/sec",
            "range": "stddev: 1.758002923558184e-7",
            "extra": "mean: 228.4026661488236 nsec\nrounds: 193088"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 7191098.482441867,
            "unit": "iter/sec",
            "range": "stddev: 1.3225288053368591e-8",
            "extra": "mean: 139.06081281484995 nsec\nrounds: 71603"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1767262.819288721,
            "unit": "iter/sec",
            "range": "stddev: 6.014116427573e-8",
            "extra": "mean: 565.8467937454118 nsec\nrounds: 82495"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1265663.3452109892,
            "unit": "iter/sec",
            "range": "stddev: 8.633266590780376e-8",
            "extra": "mean: 790.099518788938 nsec\nrounds: 62031"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4422755.234694208,
            "unit": "iter/sec",
            "range": "stddev: 3.6267957881596326e-8",
            "extra": "mean: 226.10340091975283 nsec\nrounds: 196503"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7542109.635933135,
            "unit": "iter/sec",
            "range": "stddev: 1.3099221899739637e-8",
            "extra": "mean: 132.58889730741453 nsec\nrounds: 76023"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 114019.17001755364,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010205113358224677",
            "extra": "mean: 8.770455001961922 usec\nrounds: 70892"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 66008.6021336127,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016293395805183721",
            "extra": "mean: 15.149540630717022 usec\nrounds: 48547"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 62762.76594736794,
            "unit": "iter/sec",
            "range": "stddev: 0.0000025855542224816115",
            "extra": "mean: 15.933013545620142 usec\nrounds: 43778"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1788614.4834030012,
            "unit": "iter/sec",
            "range": "stddev: 2.522930488316911e-7",
            "extra": "mean: 559.0919727416102 nsec\nrounds: 142390"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1194749.0299744513,
            "unit": "iter/sec",
            "range": "stddev: 8.80483601048808e-8",
            "extra": "mean: 836.9958668402385 nsec\nrounds: 58817"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 432061.5448695978,
            "unit": "iter/sec",
            "range": "stddev: 5.433403726812722e-7",
            "extra": "mean: 2.3144850817533738 usec\nrounds: 48196"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 62105.608936465556,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016419072991779618",
            "extra": "mean: 16.10160526761772 usec\nrounds: 17617"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 61730.3163644049,
            "unit": "iter/sec",
            "range": "stddev: 0.000001683747755824993",
            "extra": "mean: 16.199495789019196 usec\nrounds: 28022"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1727.8399284694078,
            "unit": "iter/sec",
            "range": "stddev: 0.000029960394564158758",
            "extra": "mean: 578.757316301772 usec\nrounds: 411"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 49981.044665751375,
            "unit": "iter/sec",
            "range": "stddev: 0.0000022627021713368573",
            "extra": "mean: 20.007585009227153 usec\nrounds: 25509"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 368517.8691919148,
            "unit": "iter/sec",
            "range": "stddev: 5.716504967395405e-7",
            "extra": "mean: 2.7135726204886557 usec\nrounds: 44106"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 7223.94337358451,
            "unit": "iter/sec",
            "range": "stddev: 0.000012733418865541974",
            "extra": "mean: 138.42854910195697 usec\nrounds: 5234"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 22984.146670693895,
            "unit": "iter/sec",
            "range": "stddev: 0.000053855817050728234",
            "extra": "mean: 43.5082500267481 usec\nrounds: 9339"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 240384.87275402504,
            "unit": "iter/sec",
            "range": "stddev: 8.582414381750816e-7",
            "extra": "mean: 4.159995546072714 usec\nrounds: 47374"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 255427.0100106566,
            "unit": "iter/sec",
            "range": "stddev: 8.338679440950511e-7",
            "extra": "mean: 3.9150127465309144 usec\nrounds: 97752"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 265565.43783519766,
            "unit": "iter/sec",
            "range": "stddev: 7.728964223029596e-7",
            "extra": "mean: 3.765550246868237 usec\nrounds: 102892"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 154795.93450434963,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011104072157175735",
            "extra": "mean: 6.460117981792997 usec\nrounds: 46041"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 51986.863709669924,
            "unit": "iter/sec",
            "range": "stddev: 0.000001966530896669323",
            "extra": "mean: 19.235628553872406 usec\nrounds: 22757"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 68246.38621890433,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016809974548176485",
            "extra": "mean: 14.652790505162292 usec\nrounds: 17399"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 65255.00781373808,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017190664506734584",
            "extra": "mean: 15.32449437220772 usec\nrounds: 25143"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 267022.7734355422,
            "unit": "iter/sec",
            "range": "stddev: 7.289274005343337e-7",
            "extra": "mean: 3.7449989269974924 usec\nrounds: 79215"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 238994.42912173478,
            "unit": "iter/sec",
            "range": "stddev: 8.257472575743908e-7",
            "extra": "mean: 4.184197948357355 usec\nrounds: 84517"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 286319.20767442865,
            "unit": "iter/sec",
            "range": "stddev: 8.540800668600856e-7",
            "extra": "mean: 3.492605362114204 usec\nrounds: 51584"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 329970.2031452098,
            "unit": "iter/sec",
            "range": "stddev: 6.69043835723954e-7",
            "extra": "mean: 3.0305766716758074 usec\nrounds: 96535"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 52665.59286459964,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018907143816855473",
            "extra": "mean: 18.987728906250904 usec\nrounds: 8960"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 19269.01363479046,
            "unit": "iter/sec",
            "range": "stddev: 0.0000032917399471412736",
            "extra": "mean: 51.896792381447426 usec\nrounds: 11892"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 106970.20077336747,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012422128631290208",
            "extra": "mean: 9.348397897454179 usec\nrounds: 40807"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 121559.95264253477,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011621292150591227",
            "extra": "mean: 8.226393464800449 usec\nrounds: 34031"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 31739.99124763479,
            "unit": "iter/sec",
            "range": "stddev: 0.0000026294152035339623",
            "extra": "mean: 31.505994825203935 usec\nrounds: 7923"
          }
        ]
      }
    ]
  }
}