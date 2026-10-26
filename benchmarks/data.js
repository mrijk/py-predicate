window.BENCHMARK_DATA = {
  "lastUpdate": 1793024113829,
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
          "id": "fcf872fe935513bd0727292fe211304027f74192",
          "message": "Raise benchmark alert threshold to 200% to reduce runner noise\n\nGitHub-hosted runners can vary by ~2x between runs, causing false\npositives at the previous 150% threshold.\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)",
          "timestamp": "2026-04-16T22:04:45+02:00",
          "tree_id": "cab549a003910bc21918197a19e88c30d6f4acdb",
          "url": "https://github.com/mrijk/py-predicate/commit/fcf872fe935513bd0727292fe211304027f74192"
        },
        "date": 1776369938461,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 4220447.906852929,
            "unit": "iter/sec",
            "range": "stddev: 1.5930452141032102e-7",
            "extra": "mean: 236.94167587668966 nsec\nrounds: 199641"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 7091574.626515384,
            "unit": "iter/sec",
            "range": "stddev: 1.4362725350795126e-8",
            "extra": "mean: 141.01240594169337 nsec\nrounds: 71444"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1697196.9308255988,
            "unit": "iter/sec",
            "range": "stddev: 6.367622094427409e-8",
            "extra": "mean: 589.2068161551244 nsec\nrounds: 81747"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1260141.2992645276,
            "unit": "iter/sec",
            "range": "stddev: 7.242035959078102e-8",
            "extra": "mean: 793.5618018262261 nsec\nrounds: 62736"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4267454.105098536,
            "unit": "iter/sec",
            "range": "stddev: 3.650377613869556e-8",
            "extra": "mean: 234.33175269659046 nsec\nrounds: 172414"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7604925.273652167,
            "unit": "iter/sec",
            "range": "stddev: 1.3650967731140328e-8",
            "extra": "mean: 131.49373123554216 nsec\nrounds: 77012"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 112000.27136221586,
            "unit": "iter/sec",
            "range": "stddev: 0.000001111076957883074",
            "extra": "mean: 8.928549795794133 usec\nrounds: 77436"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 65138.16084136874,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014362442464081419",
            "extra": "mean: 15.351983953543062 usec\nrounds: 48547"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 61816.91805171211,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016116316014219712",
            "extra": "mean: 16.176801295131916 usec\nrounds: 43396"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1698292.4717408153,
            "unit": "iter/sec",
            "range": "stddev: 3.0878274795379097e-7",
            "extra": "mean: 588.8267283991205 nsec\nrounds: 168862"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1157408.2724478438,
            "unit": "iter/sec",
            "range": "stddev: 7.184619119288318e-8",
            "extra": "mean: 863.9993542512569 nsec\nrounds: 57297"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 417406.4103295493,
            "unit": "iter/sec",
            "range": "stddev: 6.073568166597444e-7",
            "extra": "mean: 2.395746627873979 usec\nrounds: 38331"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 59500.92995198388,
            "unit": "iter/sec",
            "range": "stddev: 0.0000019627613914698304",
            "extra": "mean: 16.806460013431405 usec\nrounds: 17856"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 59344.3850551472,
            "unit": "iter/sec",
            "range": "stddev: 0.000001968905425690179",
            "extra": "mean: 16.850793871580702 usec\nrounds: 14913"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1672.642683360835,
            "unit": "iter/sec",
            "range": "stddev: 0.00001622446254151949",
            "extra": "mean: 597.856320389184 usec\nrounds: 412"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 47712.64952850859,
            "unit": "iter/sec",
            "range": "stddev: 0.000002542298884690515",
            "extra": "mean: 20.958802537312334 usec\nrounds: 26329"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 352819.63660872023,
            "unit": "iter/sec",
            "range": "stddev: 5.985771274576055e-7",
            "extra": "mean: 2.8343093644444965 usec\nrounds: 40344"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 6949.813288669662,
            "unit": "iter/sec",
            "range": "stddev: 0.000014922176314225109",
            "extra": "mean: 143.88875764911674 usec\nrounds: 5001"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 21951.739130973154,
            "unit": "iter/sec",
            "range": "stddev: 0.00006064443377701085",
            "extra": "mean: 45.554477211741016 usec\nrounds: 7372"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 235769.4950693648,
            "unit": "iter/sec",
            "range": "stddev: 8.480801082735371e-7",
            "extra": "mean: 4.241430808111091 usec\nrounds: 43625"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 250687.00491798593,
            "unit": "iter/sec",
            "range": "stddev: 7.687292291446906e-7",
            "extra": "mean: 3.9890380449802616 usec\nrounds: 83112"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 260203.6955506236,
            "unit": "iter/sec",
            "range": "stddev: 7.751387767319292e-7",
            "extra": "mean: 3.8431429572277005 usec\nrounds: 98435"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 151121.42940368078,
            "unit": "iter/sec",
            "range": "stddev: 0.000001053428456559945",
            "extra": "mean: 6.6171952180836335 usec\nrounds: 44540"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 51110.759228291754,
            "unit": "iter/sec",
            "range": "stddev: 0.000002113782395597807",
            "extra": "mean: 19.56535209217675 usec\nrounds: 23207"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 67537.31517433196,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018114814136361573",
            "extra": "mean: 14.806629452455006 usec\nrounds: 16705"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 63608.28675136749,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018456212611769707",
            "extra": "mean: 15.721222046253295 usec\nrounds: 25846"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 258798.13608088685,
            "unit": "iter/sec",
            "range": "stddev: 7.845755735482477e-7",
            "extra": "mean: 3.8640154644987548 usec\nrounds: 25672"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 236202.27469711236,
            "unit": "iter/sec",
            "range": "stddev: 8.605188024580007e-7",
            "extra": "mean: 4.2336594822480995 usec\nrounds: 85602"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 281929.12561332644,
            "unit": "iter/sec",
            "range": "stddev: 7.201813636836492e-7",
            "extra": "mean: 3.546990747495623 usec\nrounds: 51986"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 321734.61183473107,
            "unit": "iter/sec",
            "range": "stddev: 6.898970055161807e-7",
            "extra": "mean: 3.1081517599159674 usec\nrounds: 92251"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 52030.96102235156,
            "unit": "iter/sec",
            "range": "stddev: 0.0000022261799709301908",
            "extra": "mean: 19.219325961909835 usec\nrounds: 8320"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 19098.705831875115,
            "unit": "iter/sec",
            "range": "stddev: 0.000005506200296320441",
            "extra": "mean: 52.359568695541284 usec\nrounds: 11551"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 105937.2033692361,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014168555279488275",
            "extra": "mean: 9.439554454864886 usec\nrounds: 37765"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 121138.76395510846,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012083307425966302",
            "extra": "mean: 8.25499590181207 usec\nrounds: 33183"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 31423.960867936716,
            "unit": "iter/sec",
            "range": "stddev: 0.0000027987226837329713",
            "extra": "mean: 31.82285021937973 usec\nrounds: 7965"
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
          "id": "3441a304381f97cb91e072dcae7c47f55437c5a7",
          "message": "Add generators for is_superset_p, is_real_superset_p, and intersects_p (#212)\n\n* Add generators for is_superset_p, is_real_superset_p, and intersects_p\n\nAll three predicates were missing generate_true and generate_false\nimplementations. Added the six handlers and extended both generator test\nparametrize lists to cover the new cases.\n\n* Rewrite set generator functions to use generator expressions\n\n---------\n\nCo-authored-by: Maurits Rijk <maurits.rijk@surf.nl>",
          "timestamp": "2026-04-17T07:59:22+02:00",
          "tree_id": "13a10f0e2f00dc313501e21ad16d9209a2035a98",
          "url": "https://github.com/mrijk/py-predicate/commit/3441a304381f97cb91e072dcae7c47f55437c5a7"
        },
        "date": 1776405612130,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 4363488.396972965,
            "unit": "iter/sec",
            "range": "stddev: 1.682417480884844e-7",
            "extra": "mean: 229.1744377488706 nsec\nrounds: 196890"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 7126027.334606559,
            "unit": "iter/sec",
            "range": "stddev: 1.9773054700811203e-8",
            "extra": "mean: 140.33064329456602 nsec\nrounds: 188680"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1759904.5558627893,
            "unit": "iter/sec",
            "range": "stddev: 5.8110355457643067e-8",
            "extra": "mean: 568.2126321388788 nsec\nrounds: 83244"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1287637.8615190182,
            "unit": "iter/sec",
            "range": "stddev: 6.87528794139843e-8",
            "extra": "mean: 776.6158715000088 nsec\nrounds: 62543"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4404935.855934594,
            "unit": "iter/sec",
            "range": "stddev: 3.443881724953038e-8",
            "extra": "mean: 227.01806171654917 nsec\nrounds: 194175"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7532852.752414797,
            "unit": "iter/sec",
            "range": "stddev: 1.4472189978600923e-8",
            "extra": "mean: 132.7518315925439 nsec\nrounds: 75672"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 111731.37886430495,
            "unit": "iter/sec",
            "range": "stddev: 0.000001011474105524131",
            "extra": "mean: 8.950037224676837 usec\nrounds: 72855"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 64351.18553652872,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014217841378588485",
            "extra": "mean: 15.539729247604205 usec\nrounds: 48572"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 61016.36305666629,
            "unit": "iter/sec",
            "range": "stddev: 0.000001408686075900098",
            "extra": "mean: 16.389046313220824 usec\nrounds: 44264"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1737757.6112608712,
            "unit": "iter/sec",
            "range": "stddev: 2.5298383607106376e-7",
            "extra": "mean: 575.4542483484945 nsec\nrounds: 165262"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1159401.1049875459,
            "unit": "iter/sec",
            "range": "stddev: 7.062610395005116e-8",
            "extra": "mean: 862.514271979016 nsec\nrounds: 57301"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 419080.45481362304,
            "unit": "iter/sec",
            "range": "stddev: 6.533918682579139e-7",
            "extra": "mean: 2.386176660146864 usec\nrounds: 47396"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 60768.244466475146,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017487275285319608",
            "extra": "mean: 16.455963287728082 usec\nrounds: 18795"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 60547.331554074866,
            "unit": "iter/sec",
            "range": "stddev: 0.000002059798852186607",
            "extra": "mean: 16.51600449322691 usec\nrounds: 28716"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1723.894548487579,
            "unit": "iter/sec",
            "range": "stddev: 0.000017651667402757436",
            "extra": "mean: 580.081885447882 usec\nrounds: 419"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 48841.708732398074,
            "unit": "iter/sec",
            "range": "stddev: 0.0000023397753102258436",
            "extra": "mean: 20.47430415424168 usec\nrounds: 25257"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 359782.0892871972,
            "unit": "iter/sec",
            "range": "stddev: 7.437667038524822e-7",
            "extra": "mean: 2.779460205985259 usec\nrounds: 46338"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 6985.796826777381,
            "unit": "iter/sec",
            "range": "stddev: 0.00001325795794645289",
            "extra": "mean: 143.1475928654098 usec\nrounds: 5018"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 21966.133783317084,
            "unit": "iter/sec",
            "range": "stddev: 0.00006537690293479553",
            "extra": "mean: 45.524624854988524 usec\nrounds: 7773"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 238994.16195421317,
            "unit": "iter/sec",
            "range": "stddev: 9.163953559498964e-7",
            "extra": "mean: 4.184202625801301 usec\nrounds: 51267"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 253564.6590294888,
            "unit": "iter/sec",
            "range": "stddev: 8.026660623753514e-7",
            "extra": "mean: 3.9437672577380076 usec\nrounds: 94706"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 261081.3814722232,
            "unit": "iter/sec",
            "range": "stddev: 7.966148896242853e-7",
            "extra": "mean: 3.8302233363446154 usec\nrounds: 95157"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 155272.1370228555,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010615410914331057",
            "extra": "mean: 6.440305512461671 usec\nrounds: 45350"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 52329.53779188391,
            "unit": "iter/sec",
            "range": "stddev: 0.0000019455427760344395",
            "extra": "mean: 19.109666207582972 usec\nrounds: 23937"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 69157.88123773668,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017025327174261166",
            "extra": "mean: 14.459667967016028 usec\nrounds: 17685"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 65945.22001445416,
            "unit": "iter/sec",
            "range": "stddev: 0.0000019149619965644772",
            "extra": "mean: 15.164101352316601 usec\nrounds: 24923"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 259688.6385161063,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011619599633525196",
            "extra": "mean: 3.850765307693576 usec\nrounds: 79027"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 241039.972493138,
            "unit": "iter/sec",
            "range": "stddev: 9.155138693412774e-7",
            "extra": "mean: 4.148689487709215 usec\nrounds: 79340"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 287374.31026589684,
            "unit": "iter/sec",
            "range": "stddev: 8.385139690699061e-7",
            "extra": "mean: 3.4797821665921944 usec\nrounds: 51319"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 322496.8053274865,
            "unit": "iter/sec",
            "range": "stddev: 7.954819311966428e-7",
            "extra": "mean: 3.10080591026174 usec\nrounds: 94518"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 44613.69135518929,
            "unit": "iter/sec",
            "range": "stddev: 0.000006655356982734335",
            "extra": "mean: 22.414643792609734 usec\nrounds: 9093"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 19023.539943194217,
            "unit": "iter/sec",
            "range": "stddev: 0.0000068114737765837875",
            "extra": "mean: 52.56645203711184 usec\nrounds: 11603"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 105827.3111241313,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012920112210074679",
            "extra": "mean: 9.449356592146984 usec\nrounds: 42637"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 122182.59843299686,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012423926052159308",
            "extra": "mean: 8.184471543616624 usec\nrounds: 33630"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 31539.95856119029,
            "unit": "iter/sec",
            "range": "stddev: 0.000002627634850289435",
            "extra": "mean: 31.705812106883783 usec\nrounds: 7946"
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
          "id": "9121a2ca508ec42b3de602b4af6c1c8ba4bb3c2d",
          "message": "Refactor for loops to generator expressions (#213)\n\nReplace simple yield-in-a-loop patterns with yield from + generator\nexpressions, and inline a trivial helper function in is_instance_predicate.\n\nCo-authored-by: Maurits Rijk <maurits.rijk@surf.nl>",
          "timestamp": "2026-04-17T08:39:12+02:00",
          "tree_id": "1e6cd69c7b44182ffa0d2185cbc530fdc4d07f53",
          "url": "https://github.com/mrijk/py-predicate/commit/9121a2ca508ec42b3de602b4af6c1c8ba4bb3c2d"
        },
        "date": 1776408003310,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 4347091.026350869,
            "unit": "iter/sec",
            "range": "stddev: 1.8822984360860077e-7",
            "extra": "mean: 230.03889128115225 nsec\nrounds: 193051"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 7196578.088520418,
            "unit": "iter/sec",
            "range": "stddev: 1.2268595338224377e-8",
            "extra": "mean: 138.95492937054968 nsec\nrounds: 70792"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1725032.8766861577,
            "unit": "iter/sec",
            "range": "stddev: 9.008402485947341e-8",
            "extra": "mean: 579.6990964723127 nsec\nrounds: 83174"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1262975.1240467334,
            "unit": "iter/sec",
            "range": "stddev: 7.18722618076763e-8",
            "extra": "mean: 791.7812322350994 nsec\nrounds: 61920"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4332101.327026373,
            "unit": "iter/sec",
            "range": "stddev: 3.387833755152342e-8",
            "extra": "mean: 230.83485923133216 nsec\nrounds: 197668"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7563258.812842269,
            "unit": "iter/sec",
            "range": "stddev: 1.2834711056796887e-8",
            "extra": "mean: 132.2181383376725 nsec\nrounds: 75959"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 110681.87977070261,
            "unit": "iter/sec",
            "range": "stddev: 0.00000117152610659773",
            "extra": "mean: 9.034902570065485 usec\nrounds: 74823"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 62443.48391742796,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018619778063078064",
            "extra": "mean: 16.0144812118803 usec\nrounds: 49047"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 60969.102085107195,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015084133701368998",
            "extra": "mean: 16.401750490012024 usec\nrounds: 42856"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1617317.407681345,
            "unit": "iter/sec",
            "range": "stddev: 2.9974157227785793e-7",
            "extra": "mean: 618.3078196342686 nsec\nrounds: 169177"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1183517.8344349107,
            "unit": "iter/sec",
            "range": "stddev: 7.488546763173402e-8",
            "extra": "mean: 844.9386827174142 nsec\nrounds: 55698"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 424378.8695494693,
            "unit": "iter/sec",
            "range": "stddev: 6.094344255425894e-7",
            "extra": "mean: 2.356384994054072 usec\nrounds: 47941"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 60421.11277279712,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017919963962901279",
            "extra": "mean: 16.550506174229575 usec\nrounds: 18221"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 60940.120115080324,
            "unit": "iter/sec",
            "range": "stddev: 0.000002027094191543399",
            "extra": "mean: 16.409550852731886 usec\nrounds: 28848"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1685.425054651787,
            "unit": "iter/sec",
            "range": "stddev: 0.000017454156364639806",
            "extra": "mean: 593.3221398602043 usec\nrounds: 429"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 48631.397319009666,
            "unit": "iter/sec",
            "range": "stddev: 0.000002206378186326057",
            "extra": "mean: 20.56284736052828 usec\nrounds: 26710"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 363099.0011056302,
            "unit": "iter/sec",
            "range": "stddev: 5.840345106375066e-7",
            "extra": "mean: 2.7540698183002905 usec\nrounds: 46621"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 6913.314083086692,
            "unit": "iter/sec",
            "range": "stddev: 0.00001367505105313377",
            "extra": "mean: 144.64842591868972 usec\nrounds: 5116"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 22191.770352891843,
            "unit": "iter/sec",
            "range": "stddev: 0.000051560426558957204",
            "extra": "mean: 45.061749653050484 usec\nrounds: 10090"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 235238.71210856034,
            "unit": "iter/sec",
            "range": "stddev: 8.11177608346287e-7",
            "extra": "mean: 4.251000998247728 usec\nrounds: 46081"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 249873.98796540344,
            "unit": "iter/sec",
            "range": "stddev: 8.206846823838613e-7",
            "extra": "mean: 4.0020172093241495 usec\nrounds: 95239"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 257506.8944144544,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011628216871371756",
            "extra": "mean: 3.883391170065184 usec\nrounds: 31076"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 145164.45565731553,
            "unit": "iter/sec",
            "range": "stddev: 0.000002421285344851142",
            "extra": "mean: 6.888738675538203 usec\nrounds: 43490"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 50265.44352940262,
            "unit": "iter/sec",
            "range": "stddev: 0.000020908839497247953",
            "extra": "mean: 19.894383293664823 usec\nrounds: 24793"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 68350.43064503308,
            "unit": "iter/sec",
            "range": "stddev: 0.000001675697139192788",
            "extra": "mean: 14.630485727198097 usec\nrounds: 17726"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 64739.69130677336,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017200789229743596",
            "extra": "mean: 15.446474640440176 usec\nrounds: 26420"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 261430.4236471888,
            "unit": "iter/sec",
            "range": "stddev: 7.973235338384856e-7",
            "extra": "mean: 3.8251095111621036 usec\nrounds: 82156"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 237100.19589764482,
            "unit": "iter/sec",
            "range": "stddev: 7.823388034055591e-7",
            "extra": "mean: 4.217626207410204 usec\nrounds: 85823"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 284771.0150307174,
            "unit": "iter/sec",
            "range": "stddev: 8.367162803354958e-7",
            "extra": "mean: 3.511593340678064 usec\nrounds: 45350"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 327610.25257027947,
            "unit": "iter/sec",
            "range": "stddev: 6.91203167574233e-7",
            "extra": "mean: 3.0524075243508397 usec\nrounds: 99118"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 52347.51852653027,
            "unit": "iter/sec",
            "range": "stddev: 0.0000020287111048326844",
            "extra": "mean: 19.103102270133196 usec\nrounds: 8722"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 19289.593593030262,
            "unit": "iter/sec",
            "range": "stddev: 0.000003949337296735194",
            "extra": "mean: 51.8414239873525 usec\nrounds: 11406"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 105709.86409431881,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012454988791467898",
            "extra": "mean: 9.459855128635468 usec\nrounds: 41278"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 121809.7203186244,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013697553128058035",
            "extra": "mean: 8.209525458101743 usec\nrounds: 35470"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 31769.182892673995,
            "unit": "iter/sec",
            "range": "stddev: 0.000003242072625682061",
            "extra": "mean: 31.477045014922336 usec\nrounds: 8064"
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
          "id": "26bff45b7a06f4953ada230128de3d4f0fa60f0a",
          "message": "Prefer stdlib itertools over more-itertools where possible (#214)\n\n- Replace more_itertools.pairwise with itertools.pairwise (available since Python 3.10)\n- Replace list concatenation with itertools.chain in generate_false.py\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)",
          "timestamp": "2026-04-17T08:54:42+02:00",
          "tree_id": "042704e80b4ff3a91ae9c70098e7f809d210609e",
          "url": "https://github.com/mrijk/py-predicate/commit/26bff45b7a06f4953ada230128de3d4f0fa60f0a"
        },
        "date": 1776408963457,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 4189553.5820526136,
            "unit": "iter/sec",
            "range": "stddev: 1.5208162886706694e-7",
            "extra": "mean: 238.68891527819153 nsec\nrounds: 183487"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 6913282.016533224,
            "unit": "iter/sec",
            "range": "stddev: 4.02489044558403e-8",
            "extra": "mean: 144.64909685565902 nsec\nrounds: 197278"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1719861.338945994,
            "unit": "iter/sec",
            "range": "stddev: 6.773596710191419e-8",
            "extra": "mean: 581.4422229020181 nsec\nrounds: 81740"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1270870.2119628186,
            "unit": "iter/sec",
            "range": "stddev: 7.990692368110098e-8",
            "extra": "mean: 786.8624117450449 nsec\nrounds: 62461"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4398692.739303515,
            "unit": "iter/sec",
            "range": "stddev: 3.3248725825361104e-8",
            "extra": "mean: 227.340271136633 nsec\nrounds: 196117"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7537932.083397243,
            "unit": "iter/sec",
            "range": "stddev: 1.4660933614060547e-8",
            "extra": "mean: 132.66237861210786 nsec\nrounds: 76717"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 117603.58513181299,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011895682087689324",
            "extra": "mean: 8.503142135328403 usec\nrounds: 74218"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 64861.32710759545,
            "unit": "iter/sec",
            "range": "stddev: 0.000001494267569213446",
            "extra": "mean: 15.417507544073937 usec\nrounds: 50437"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 62520.61961335334,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015019255670051206",
            "extra": "mean: 15.994723119897186 usec\nrounds: 43322"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1637665.1377341792,
            "unit": "iter/sec",
            "range": "stddev: 2.644100023587526e-7",
            "extra": "mean: 610.6254428689664 nsec\nrounds: 162576"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1192707.2688068014,
            "unit": "iter/sec",
            "range": "stddev: 8.22275357249397e-8",
            "extra": "mean: 838.4286959200074 nsec\nrounds: 56745"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 403682.7616233023,
            "unit": "iter/sec",
            "range": "stddev: 5.79702590840823e-7",
            "extra": "mean: 2.4771927242539844 usec\nrounds: 48105"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 61180.907933408926,
            "unit": "iter/sec",
            "range": "stddev: 0.0000024931010428163548",
            "extra": "mean: 16.344968287957233 usec\nrounds: 18195"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 61207.269590792304,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018960083730622045",
            "extra": "mean: 16.337928593868117 usec\nrounds: 28625"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1709.0159952838505,
            "unit": "iter/sec",
            "range": "stddev: 0.00002325364555832637",
            "extra": "mean: 585.1320308057796 usec\nrounds: 422"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 48964.51410011326,
            "unit": "iter/sec",
            "range": "stddev: 0.0000021396245908361798",
            "extra": "mean: 20.42295360994273 usec\nrounds: 27161"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 353615.42373492755,
            "unit": "iter/sec",
            "range": "stddev: 6.46401877032399e-7",
            "extra": "mean: 2.82793094667049 usec\nrounds: 46732"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 7079.990249138499,
            "unit": "iter/sec",
            "range": "stddev: 0.00001312480103055978",
            "extra": "mean: 141.24313237884488 usec\nrounds: 5099"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 22276.99608947671,
            "unit": "iter/sec",
            "range": "stddev: 0.00006274623658015931",
            "extra": "mean: 44.88935563769227 usec\nrounds: 8115"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 234592.78035114257,
            "unit": "iter/sec",
            "range": "stddev: 8.405803143756084e-7",
            "extra": "mean: 4.262705776806867 usec\nrounds: 46254"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 247494.24470220396,
            "unit": "iter/sec",
            "range": "stddev: 8.183258200922591e-7",
            "extra": "mean: 4.040497997047343 usec\nrounds: 89119"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 256630.52712470348,
            "unit": "iter/sec",
            "range": "stddev: 0.000001367489135625109",
            "extra": "mean: 3.8966525580726175 usec\nrounds: 93371"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 131756.46705933317,
            "unit": "iter/sec",
            "range": "stddev: 0.000007310191279413052",
            "extra": "mean: 7.589760277570858 usec\nrounds: 45536"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 49731.27900117638,
            "unit": "iter/sec",
            "range": "stddev: 0.0000021486299303497814",
            "extra": "mean: 20.108069208844302 usec\nrounds: 22815"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 66339.651608952,
            "unit": "iter/sec",
            "range": "stddev: 0.000002542325941282813",
            "extra": "mean: 15.073941085711972 usec\nrounds: 18145"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 65066.28410736947,
            "unit": "iter/sec",
            "range": "stddev: 0.000001898558172389479",
            "extra": "mean: 15.368942820675677 usec\nrounds: 26653"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 257157.1457982457,
            "unit": "iter/sec",
            "range": "stddev: 8.149168537044627e-7",
            "extra": "mean: 3.88867280703355 usec\nrounds: 77737"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 233694.1716558012,
            "unit": "iter/sec",
            "range": "stddev: 9.577101293309334e-7",
            "extra": "mean: 4.279096876548809 usec\nrounds: 83529"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 274996.21591482294,
            "unit": "iter/sec",
            "range": "stddev: 7.962879819612665e-7",
            "extra": "mean: 3.636413674542122 usec\nrounds: 48572"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 322334.0593825297,
            "unit": "iter/sec",
            "range": "stddev: 7.168815748470123e-7",
            "extra": "mean: 3.102371502147872 usec\nrounds: 99811"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 51242.22629693389,
            "unit": "iter/sec",
            "range": "stddev: 0.0000019637025979275137",
            "extra": "mean: 19.515155219940855 usec\nrounds: 7615"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 18882.326902581422,
            "unit": "iter/sec",
            "range": "stddev: 0.0000036241002736124673",
            "extra": "mean: 52.959574588409914 usec\nrounds: 12026"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 102336.44142916088,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014760545014489598",
            "extra": "mean: 9.771690182252604 usec\nrounds: 40427"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 118698.70793406999,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013765113607881275",
            "extra": "mean: 8.42469153544148 usec\nrounds: 36257"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 30788.05356389526,
            "unit": "iter/sec",
            "range": "stddev: 0.000002808666234448605",
            "extra": "mean: 32.48013057807223 usec\nrounds: 8202"
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
          "id": "156ebed327e6c8a00baf382c08ff7b96a0c39b80",
          "message": "Generalize predicates to broader abstract types (#214)\n\n- Set predicates (is_subset_p, is_superset_p, intersects_p, etc.) now\n  accept AbstractSet[T] instead of set[T], enabling use with frozenset\n  and other Set-like types\n- HasKeyPredicate, DictOfPredicate, StructPredicate, HasPathPredicate\n  now accept Mapping instead of dict\n- ConstrainedT extended with date, Decimal, and Fraction\n- Fix implies.py to use <= instead of .issubset() for AbstractSet\n\nCo-authored-by: Maurits Rijk <maurits.rijk@surf.nl>",
          "timestamp": "2026-04-17T09:59:06+02:00",
          "tree_id": "470d63ee578bd7ec24bc094773f2acecfec83f18",
          "url": "https://github.com/mrijk/py-predicate/commit/156ebed327e6c8a00baf382c08ff7b96a0c39b80"
        },
        "date": 1776412794224,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 7977817.106279295,
            "unit": "iter/sec",
            "range": "stddev: 2.1184055827972708e-8",
            "extra": "mean: 125.34757148204181 nsec\nrounds: 199601"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 7284615.668391136,
            "unit": "iter/sec",
            "range": "stddev: 1.2592849594482967e-8",
            "extra": "mean: 137.27560183293207 nsec\nrounds: 70493"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1680729.739681601,
            "unit": "iter/sec",
            "range": "stddev: 6.444828761999935e-8",
            "extra": "mean: 594.9796546049342 nsec\nrounds: 81414"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1261709.513024345,
            "unit": "iter/sec",
            "range": "stddev: 6.93841397628657e-8",
            "extra": "mean: 792.5754618453959 nsec\nrounds: 61763"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4349218.713157707,
            "unit": "iter/sec",
            "range": "stddev: 3.5511618791335314e-8",
            "extra": "mean: 229.9263536631755 nsec\nrounds: 196079"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7593955.630014748,
            "unit": "iter/sec",
            "range": "stddev: 1.3087335122720037e-8",
            "extra": "mean: 131.68367695586048 nsec\nrounds: 75160"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 117150.63354528278,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010867556085473358",
            "extra": "mean: 8.536018711443546 usec\nrounds: 74767"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 65224.81871691837,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013769857270905793",
            "extra": "mean: 15.331587264965666 usec\nrounds: 49831"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 61700.40147526687,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015915849014626868",
            "extra": "mean: 16.207349970013702 usec\nrounds: 45021"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1563532.1231058135,
            "unit": "iter/sec",
            "range": "stddev: 3.0566569357938774e-7",
            "extra": "mean: 639.5775214477791 nsec\nrounds: 151700"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1226085.4026272506,
            "unit": "iter/sec",
            "range": "stddev: 7.778374930363436e-8",
            "extra": "mean: 815.6038705437682 nsec\nrounds: 56297"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 407554.1465263291,
            "unit": "iter/sec",
            "range": "stddev: 7.703242369961156e-7",
            "extra": "mean: 2.4536616999807586 usec\nrounds: 46577"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 60931.914025263235,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017637953990420703",
            "extra": "mean: 16.411760831694632 usec\nrounds: 18372"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 61247.62115352557,
            "unit": "iter/sec",
            "range": "stddev: 0.00000179705180416676",
            "extra": "mean: 16.327164731726686 usec\nrounds: 28683"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1696.8799451886023,
            "unit": "iter/sec",
            "range": "stddev: 0.000046594236825482166",
            "extra": "mean: 589.3168829270674 usec\nrounds: 410"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 49265.83237955913,
            "unit": "iter/sec",
            "range": "stddev: 0.0000020416373221798104",
            "extra": "mean: 20.29804332332584 usec\nrounds: 26660"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 359631.26722722175,
            "unit": "iter/sec",
            "range": "stddev: 6.361093711914569e-7",
            "extra": "mean: 2.780625855226824 usec\nrounds: 47062"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 7001.3665419160525,
            "unit": "iter/sec",
            "range": "stddev: 0.000014960015899552693",
            "extra": "mean: 142.82925968997068 usec\nrounds: 5676"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 22033.04185605159,
            "unit": "iter/sec",
            "range": "stddev: 0.00005889641381449527",
            "extra": "mean: 45.38637953548571 usec\nrounds: 10721"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 235876.6071267548,
            "unit": "iter/sec",
            "range": "stddev: 8.519678964503329e-7",
            "extra": "mean: 4.239504765568475 usec\nrounds: 54663"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 247829.0720515127,
            "unit": "iter/sec",
            "range": "stddev: 9.265022779358479e-7",
            "extra": "mean: 4.035039116767319 usec\nrounds: 90984"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 262042.45678194042,
            "unit": "iter/sec",
            "range": "stddev: 7.600336142108075e-7",
            "extra": "mean: 3.816175486524894 usec\nrounds: 102156"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 153105.87175075675,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010899978541330867",
            "extra": "mean: 6.531428145537843 usec\nrounds: 45954"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 50862.714173215485,
            "unit": "iter/sec",
            "range": "stddev: 0.0000020574763468430372",
            "extra": "mean: 19.660767543675522 usec\nrounds: 25123"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 67473.19945472798,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018094955111755682",
            "extra": "mean: 14.820699301075281 usec\nrounds: 18171"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 63948.20783942089,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017154835879566678",
            "extra": "mean: 15.637654811391755 usec\nrounds: 27414"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 257292.07394702028,
            "unit": "iter/sec",
            "range": "stddev: 7.884570122303456e-7",
            "extra": "mean: 3.886633523759122 usec\nrounds: 82974"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 232646.42651033239,
            "unit": "iter/sec",
            "range": "stddev: 9.021314768570806e-7",
            "extra": "mean: 4.298368193313245 usec\nrounds: 81813"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 280507.89702402294,
            "unit": "iter/sec",
            "range": "stddev: 7.056651475114904e-7",
            "extra": "mean: 3.564962022849428 usec\nrounds: 51057"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 321445.13140875846,
            "unit": "iter/sec",
            "range": "stddev: 7.164960421477244e-7",
            "extra": "mean: 3.1109508351158457 usec\nrounds: 109326"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 52075.83796151433,
            "unit": "iter/sec",
            "range": "stddev: 0.0000019877312385912477",
            "extra": "mean: 19.20276349156458 usec\nrounds: 9543"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 19142.648482737655,
            "unit": "iter/sec",
            "range": "stddev: 0.0000032309204072021616",
            "extra": "mean: 52.239375387463966 usec\nrounds: 11937"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 105712.81934860357,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013446239422308627",
            "extra": "mean: 9.459590673694482 usec\nrounds: 43061"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 120847.77824636122,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011482840009076327",
            "extra": "mean: 8.274872856672566 usec\nrounds: 38083"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 31320.884922040976,
            "unit": "iter/sec",
            "range": "stddev: 0.0000023144264376691995",
            "extra": "mean: 31.92757811565806 usec\nrounds: 8353"
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
          "id": "fc5ebcf9acd9342377f1cf0239aee0d286f14a4f",
          "message": "Generalize HasKeyPredicate to accept a Predicate[T] instead of a fixed key\n\nhas_key_p now takes a key_p: Predicate[T], enabling flexible key matching\nlike has_key_p(starts_with_p(\"_\")) in addition to has_key_p(eq_p(\"name\")).",
          "timestamp": "2026-04-17T10:29:58+02:00",
          "tree_id": "0cf44db8bb9f3360744b49f1ab165da9095f46a4",
          "url": "https://github.com/mrijk/py-predicate/commit/fc5ebcf9acd9342377f1cf0239aee0d286f14a4f"
        },
        "date": 1776415184232,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 8019965.857620594,
            "unit": "iter/sec",
            "range": "stddev: 2.5935102626148747e-8",
            "extra": "mean: 124.68881012127967 nsec\nrounds: 197239"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 7028713.496697733,
            "unit": "iter/sec",
            "range": "stddev: 2.1170313316430195e-8",
            "extra": "mean: 142.27354699687575 nsec\nrounds: 194553"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1680997.2530348296,
            "unit": "iter/sec",
            "range": "stddev: 5.931078200246679e-8",
            "extra": "mean: 594.8849697372351 nsec\nrounds: 81948"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1258336.0977107075,
            "unit": "iter/sec",
            "range": "stddev: 1.4461749777157153e-7",
            "extra": "mean: 794.7002409128222 nsec\nrounds: 62263"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4382698.667874585,
            "unit": "iter/sec",
            "range": "stddev: 3.740849853972516e-8",
            "extra": "mean: 228.16991898851117 nsec\nrounds: 196503"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7571853.61647389,
            "unit": "iter/sec",
            "range": "stddev: 1.2506179198314436e-8",
            "extra": "mean: 132.06805765821005 nsec\nrounds: 75965"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 115793.23112789573,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014800078605974102",
            "extra": "mean: 8.636083389844107 usec\nrounds: 76664"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 64763.692080379325,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015270509424960736",
            "extra": "mean: 15.440750332128733 usec\nrounds: 48172"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 62776.11780124177,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015122936780963668",
            "extra": "mean: 15.929624752619203 usec\nrounds: 45474"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1758489.6736180207,
            "unit": "iter/sec",
            "range": "stddev: 2.737799326798394e-7",
            "extra": "mean: 568.6698164923203 nsec\nrounds: 162549"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1169902.5306614765,
            "unit": "iter/sec",
            "range": "stddev: 7.414615951419003e-8",
            "extra": "mean: 854.7720633056399 nsec\nrounds: 56424"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 430844.5068236051,
            "unit": "iter/sec",
            "range": "stddev: 5.922816900945087e-7",
            "extra": "mean: 2.3210229773439277 usec\nrounds: 48265"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 60374.044833961794,
            "unit": "iter/sec",
            "range": "stddev: 0.000001937449173965588",
            "extra": "mean: 16.56340904026157 usec\nrounds: 19734"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 59990.887561409174,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017519348145422885",
            "extra": "mean: 16.66919828409537 usec\nrounds: 30073"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1673.5256627201272,
            "unit": "iter/sec",
            "range": "stddev: 0.00005311119849400882",
            "extra": "mean: 597.5408816705043 usec\nrounds: 431"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 48725.77532736464,
            "unit": "iter/sec",
            "range": "stddev: 0.0000022633396955612526",
            "extra": "mean: 20.523018736623264 usec\nrounds: 29461"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 361878.84139173356,
            "unit": "iter/sec",
            "range": "stddev: 5.970506294143657e-7",
            "extra": "mean: 2.7633558131062457 usec\nrounds: 52477"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 7022.354153164817,
            "unit": "iter/sec",
            "range": "stddev: 0.000013238404797058599",
            "extra": "mean: 142.4023878871621 usec\nrounds: 5102"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 22213.389487228025,
            "unit": "iter/sec",
            "range": "stddev: 0.00005518975447455306",
            "extra": "mean: 45.017893400508164 usec\nrounds: 10713"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 239827.21651895792,
            "unit": "iter/sec",
            "range": "stddev: 9.965329707826899e-7",
            "extra": "mean: 4.169668541022123 usec\nrounds: 58333"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 257350.99785107237,
            "unit": "iter/sec",
            "range": "stddev: 7.430902983806934e-7",
            "extra": "mean: 3.885743627769785 usec\nrounds: 103221"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 264823.61702662427,
            "unit": "iter/sec",
            "range": "stddev: 7.827687577506363e-7",
            "extra": "mean: 3.77609826203478 usec\nrounds: 111396"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 155924.8098889067,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010965856365279313",
            "extra": "mean: 6.413347566128059 usec\nrounds: 51852"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 52667.746189992184,
            "unit": "iter/sec",
            "range": "stddev: 0.000002115830689866715",
            "extra": "mean: 18.986952591299946 usec\nrounds: 25818"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 69410.82739098737,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016177184082938032",
            "extra": "mean: 14.406974208318468 usec\nrounds: 18727"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 66112.29287232572,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016501773538639266",
            "extra": "mean: 15.12578004110632 usec\nrounds: 28228"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 258261.96694476425,
            "unit": "iter/sec",
            "range": "stddev: 7.892474406467037e-7",
            "extra": "mean: 3.872037419330407 usec\nrounds: 98532"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 237546.39571386797,
            "unit": "iter/sec",
            "range": "stddev: 9.649655961510442e-7",
            "extra": "mean: 4.209703948547934 usec\nrounds: 98922"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 289686.7708551061,
            "unit": "iter/sec",
            "range": "stddev: 7.596923548455637e-7",
            "extra": "mean: 3.452004373717757 usec\nrounds: 58303"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 329649.59946267784,
            "unit": "iter/sec",
            "range": "stddev: 6.674826050802298e-7",
            "extra": "mean: 3.0335240862721498 usec\nrounds: 110291"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 52351.136864287415,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017508520354696584",
            "extra": "mean: 19.101781926767934 usec\nrounds: 9882"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 19324.412393413557,
            "unit": "iter/sec",
            "range": "stddev: 0.00000331463008954269",
            "extra": "mean: 51.74801591073659 usec\nrounds: 12633"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 106679.09070246607,
            "unit": "iter/sec",
            "range": "stddev: 0.000001250668467343789",
            "extra": "mean: 9.37390817089973 usec\nrounds: 22825"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 124084.22130833926,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011980897111941282",
            "extra": "mean: 8.059042394399855 usec\nrounds: 41798"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 32100.05170562222,
            "unit": "iter/sec",
            "range": "stddev: 0.0000031236295333132623",
            "extra": "mean: 31.15259779549991 usec\nrounds: 9254"
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
          "id": "9546d51851017913d339dba063736f60a3e7a66a",
          "message": "Add documentation for has_key_p and other undocumented predicates\n\n- Add docs/has_key_p.rst with full examples showing the generic key_p pattern\n- Add has_key_p, has_path_p, comp_p to standard_predicates.rst\n- Add range predicates: ge_le_p, ge_lt_p, gt_le_p, gt_lt_p\n- Add numeric predicates: is_even_p, is_odd_p, neg_p, pos_p\n- Add is_not_empty_p, match_p, regex_p",
          "timestamp": "2026-04-17T10:47:53+02:00",
          "tree_id": "949c9bf52682b858a1f3ec4d575bb9905d7918c7",
          "url": "https://github.com/mrijk/py-predicate/commit/9546d51851017913d339dba063736f60a3e7a66a"
        },
        "date": 1776415782303,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 8867520.371455645,
            "unit": "iter/sec",
            "range": "stddev: 1.1019469756271368e-8",
            "extra": "mean: 112.77109700463483 nsec\nrounds: 194402"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 7831682.926424661,
            "unit": "iter/sec",
            "range": "stddev: 1.454839911987165e-8",
            "extra": "mean: 127.68647676298642 nsec\nrounds: 197123"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1841911.847311791,
            "unit": "iter/sec",
            "range": "stddev: 3.809022749157477e-8",
            "extra": "mean: 542.9141473081172 nsec\nrounds: 90367"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1256725.6559142142,
            "unit": "iter/sec",
            "range": "stddev: 4.757397666592083e-8",
            "extra": "mean: 795.7186163057543 nsec\nrounds: 60909"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4505516.983176852,
            "unit": "iter/sec",
            "range": "stddev: 2.3318671892075095e-8",
            "extra": "mean: 221.95011221440282 nsec\nrounds: 191461"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 8440908.021107249,
            "unit": "iter/sec",
            "range": "stddev: 7.993129552833403e-9",
            "extra": "mean: 118.4706666035704 nsec\nrounds: 84353"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 129652.72462832829,
            "unit": "iter/sec",
            "range": "stddev: 6.274736009926565e-7",
            "extra": "mean: 7.712911571019204 usec\nrounds: 83536"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 74369.52119089257,
            "unit": "iter/sec",
            "range": "stddev: 9.173432080319009e-7",
            "extra": "mean: 13.44636867344067 usec\nrounds: 53961"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 72203.26383007312,
            "unit": "iter/sec",
            "range": "stddev: 0.000001350406473279635",
            "extra": "mean: 13.84978942715736 usec\nrounds: 48672"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1820058.7589523357,
            "unit": "iter/sec",
            "range": "stddev: 1.9436252219929342e-7",
            "extra": "mean: 549.4328109360716 nsec\nrounds: 161031"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1263618.1978811757,
            "unit": "iter/sec",
            "range": "stddev: 1.1729221062078082e-7",
            "extra": "mean: 791.3782831529267 nsec\nrounds: 63308"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 451535.38561359065,
            "unit": "iter/sec",
            "range": "stddev: 3.237950361529503e-7",
            "extra": "mean: 2.214665853133751 usec\nrounds: 47524"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 60034.898337018094,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013370238750008085",
            "extra": "mean: 16.65697831928184 usec\nrounds: 17527"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 60231.121568839786,
            "unit": "iter/sec",
            "range": "stddev: 9.575182044830448e-7",
            "extra": "mean: 16.60271258367774 usec\nrounds: 19978"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1720.8815469924498,
            "unit": "iter/sec",
            "range": "stddev: 0.000011722035725731888",
            "extra": "mean: 581.0975204816857 usec\nrounds: 415"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 47563.481097059936,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015337293969074693",
            "extra": "mean: 21.024533464221427 usec\nrounds: 23458"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 400701.2578063695,
            "unit": "iter/sec",
            "range": "stddev: 3.6392467932261396e-7",
            "extra": "mean: 2.495624809052207 usec\nrounds: 42581"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 7508.1080381527745,
            "unit": "iter/sec",
            "range": "stddev: 0.000011938001810940612",
            "extra": "mean: 133.18934609337757 usec\nrounds: 5721"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 22608.158302175,
            "unit": "iter/sec",
            "range": "stddev: 0.00020591778254206542",
            "extra": "mean: 44.23182050630792 usec\nrounds: 8329"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 263882.44608946756,
            "unit": "iter/sec",
            "range": "stddev: 7.710208647022555e-7",
            "extra": "mean: 3.7895662057829975 usec\nrounds: 55418"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 280019.3814295851,
            "unit": "iter/sec",
            "range": "stddev: 4.6949988794132124e-7",
            "extra": "mean: 3.5711813764272042 usec\nrounds: 78180"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 286412.1844774375,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015700046792393465",
            "extra": "mean: 3.4914715720789324 usec\nrounds: 87889"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 171330.80591450012,
            "unit": "iter/sec",
            "range": "stddev: 7.690190378622735e-7",
            "extra": "mean: 5.836661974840846 usec\nrounds: 23516"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 57529.35655609119,
            "unit": "iter/sec",
            "range": "stddev: 0.000002126922229245423",
            "extra": "mean: 17.382429769138803 usec\nrounds: 21230"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 76350.32548063099,
            "unit": "iter/sec",
            "range": "stddev: 0.000001155286016582621",
            "extra": "mean: 13.0975211134324 usec\nrounds: 17453"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 73048.48586627313,
            "unit": "iter/sec",
            "range": "stddev: 0.000001206094327875993",
            "extra": "mean: 13.689537683651091 usec\nrounds: 24029"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 285352.610115205,
            "unit": "iter/sec",
            "range": "stddev: 6.189501469130872e-7",
            "extra": "mean: 3.5044361416433913 usec\nrounds: 74031"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 263580.49899093225,
            "unit": "iter/sec",
            "range": "stddev: 5.008900158367467e-7",
            "extra": "mean: 3.7939073786881417 usec\nrounds: 75609"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 324046.49307947146,
            "unit": "iter/sec",
            "range": "stddev: 4.822328263092308e-7",
            "extra": "mean: 3.085976924165487 usec\nrounds: 50746"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 352273.44127322134,
            "unit": "iter/sec",
            "range": "stddev: 6.107771325180487e-7",
            "extra": "mean: 2.8387039238203755 usec\nrounds: 95239"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 59208.99874188513,
            "unit": "iter/sec",
            "range": "stddev: 0.000001130478421770612",
            "extra": "mean: 16.889324617012793 usec\nrounds: 9140"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 22025.670277015517,
            "unit": "iter/sec",
            "range": "stddev: 0.0000021176089837326445",
            "extra": "mean: 45.40156950608362 usec\nrounds: 11891"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 119335.98010896653,
            "unit": "iter/sec",
            "range": "stddev: 7.693714553280475e-7",
            "extra": "mean: 8.379702409004334 usec\nrounds: 35784"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 137912.81895967462,
            "unit": "iter/sec",
            "range": "stddev: 8.080684759545493e-7",
            "extra": "mean: 7.250957579892537 usec\nrounds: 31235"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 36677.232402911555,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014415725489949887",
            "extra": "mean: 27.26487072455927 usec\nrounds: 7016"
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
          "id": "f89c62a2fe01efec38964bb07d4515b4f0ee412c",
          "message": "Fix three inconsistencies in predicate.py (#215)\n\n* Fix three inconsistencies in predicate.py\n\n- __xor__: call resolve_predicate() like __and__ and __or__ already do\n- OrPredicate.__repr__: use !r format spec consistently with And/XorPredicate\n- Remove stray backtick fences from And/Or/Xor/NotPredicate docstrings\n\n* Remove get_klass indirection: make klass an abstract property\n\n- Replace the klass/get_klass two-level pattern with a single\n  abstract klass property on the base Predicate class\n- Remove commented-out @abstractmethod on get_klass\n- Update all 20 predicate subclasses to override klass directly\n\n* Drop @abstractmethod from klass — not all predicates implement it\n\n---------\n\nCo-authored-by: Maurits Rijk <maurits.rijk@surf.nl>",
          "timestamp": "2026-04-17T14:57:50+02:00",
          "tree_id": "7501ed7950d22070e9740665985e8f25522b3c66",
          "url": "https://github.com/mrijk/py-predicate/commit/f89c62a2fe01efec38964bb07d4515b4f0ee412c"
        },
        "date": 1776430718214,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 8670574.989106303,
            "unit": "iter/sec",
            "range": "stddev: 1.1099119951184182e-8",
            "extra": "mean: 115.3326049606166 nsec\nrounds: 193499"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 7610940.057431647,
            "unit": "iter/sec",
            "range": "stddev: 1.4303094423464322e-8",
            "extra": "mean: 131.38981419562717 nsec\nrounds: 199961"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1775422.0028489816,
            "unit": "iter/sec",
            "range": "stddev: 3.774239774442482e-8",
            "extra": "mean: 563.2463709446664 nsec\nrounds: 70652"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1216688.819823154,
            "unit": "iter/sec",
            "range": "stddev: 9.419666336975041e-8",
            "extra": "mean: 821.9028429515364 nsec\nrounds: 61204"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4429830.242600796,
            "unit": "iter/sec",
            "range": "stddev: 2.089487367387042e-8",
            "extra": "mean: 225.7422847456318 nsec\nrounds: 193987"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 8266672.034510236,
            "unit": "iter/sec",
            "range": "stddev: 1.0471811787581967e-8",
            "extra": "mean: 120.9676633868354 nsec\nrounds: 66468"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 129042.63978620914,
            "unit": "iter/sec",
            "range": "stddev: 5.898883182494511e-7",
            "extra": "mean: 7.749376498006751 usec\nrounds: 74683"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 74030.59887615907,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010252324210178996",
            "extra": "mean: 13.507928007888122 usec\nrounds: 45755"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 72336.68156777578,
            "unit": "iter/sec",
            "range": "stddev: 8.871927029394692e-7",
            "extra": "mean: 13.824244882771557 usec\nrounds: 43041"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1850530.152232148,
            "unit": "iter/sec",
            "range": "stddev: 1.7862855456474675e-7",
            "extra": "mean: 540.3856828778387 nsec\nrounds: 182816"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1250934.2460206663,
            "unit": "iter/sec",
            "range": "stddev: 4.4060022657445175e-8",
            "extra": "mean: 799.4025290946263 nsec\nrounds: 48634"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 456683.23272953,
            "unit": "iter/sec",
            "range": "stddev: 3.031769080703297e-7",
            "extra": "mean: 2.1897015881733686 usec\nrounds: 39479"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 59794.71431057732,
            "unit": "iter/sec",
            "range": "stddev: 0.00000112527803719824",
            "extra": "mean: 16.723886241950087 usec\nrounds: 17001"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 58483.07690933961,
            "unit": "iter/sec",
            "range": "stddev: 0.000002424950544894497",
            "extra": "mean: 17.098963543764956 usec\nrounds: 24550"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1711.2657081221384,
            "unit": "iter/sec",
            "range": "stddev: 0.000012048709834027463",
            "extra": "mean: 584.3627878790094 usec\nrounds: 462"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 47608.89183360186,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015491216177530126",
            "extra": "mean: 21.00447965676467 usec\nrounds: 23890"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 394966.05906778557,
            "unit": "iter/sec",
            "range": "stddev: 3.51270464529993e-7",
            "extra": "mean: 2.5318631235307643 usec\nrounds: 44405"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 7434.004111079141,
            "unit": "iter/sec",
            "range": "stddev: 0.000012895696990994972",
            "extra": "mean: 134.51700928032406 usec\nrounds: 5711"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 23498.615908139236,
            "unit": "iter/sec",
            "range": "stddev: 0.00008347241837263079",
            "extra": "mean: 42.55569791468565 usec\nrounds: 10646"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 263802.16907736624,
            "unit": "iter/sec",
            "range": "stddev: 5.382289850454534e-7",
            "extra": "mean: 3.790719399682897 usec\nrounds: 53970"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 276302.9029413551,
            "unit": "iter/sec",
            "range": "stddev: 5.355844741613221e-7",
            "extra": "mean: 3.6192164083496747 usec\nrounds: 79618"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 283606.34053056844,
            "unit": "iter/sec",
            "range": "stddev: 4.20412354973898e-7",
            "extra": "mean: 3.5260142566954182 usec\nrounds: 88590"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 168710.54739745957,
            "unit": "iter/sec",
            "range": "stddev: 5.430958374090026e-7",
            "extra": "mean: 5.927311691095005 usec\nrounds: 46668"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 57558.667902302,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010473222895398365",
            "extra": "mean: 17.37357788921321 usec\nrounds: 22930"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 75583.88274943872,
            "unit": "iter/sec",
            "range": "stddev: 7.954214118014024e-7",
            "extra": "mean: 13.23033381752839 usec\nrounds: 18588"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 72002.73229405202,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011569008176809166",
            "extra": "mean: 13.888361845993552 usec\nrounds: 23662"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 280560.8336325296,
            "unit": "iter/sec",
            "range": "stddev: 4.987091518859218e-7",
            "extra": "mean: 3.5642893808541034 usec\nrounds: 85911"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 262369.0291050493,
            "unit": "iter/sec",
            "range": "stddev: 4.581110042347469e-7",
            "extra": "mean: 3.8114254697326047 usec\nrounds: 85529"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 315496.56831958913,
            "unit": "iter/sec",
            "range": "stddev: 4.293407556875697e-7",
            "extra": "mean: 3.1696065834447626 usec\nrounds: 50946"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 339666.68415030907,
            "unit": "iter/sec",
            "range": "stddev: 4.5641591649610224e-7",
            "extra": "mean: 2.944062655133645 usec\nrounds: 99513"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 59347.06530382658,
            "unit": "iter/sec",
            "range": "stddev: 9.193279001731913e-7",
            "extra": "mean: 16.850032851338344 usec\nrounds: 10167"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 21645.242425311262,
            "unit": "iter/sec",
            "range": "stddev: 0.000002071019911962929",
            "extra": "mean: 46.199528762525276 usec\nrounds: 11960"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 117798.4766841329,
            "unit": "iter/sec",
            "range": "stddev: 7.212492325933474e-7",
            "extra": "mean: 8.489074121742842 usec\nrounds: 40393"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 137085.4342803604,
            "unit": "iter/sec",
            "range": "stddev: 5.768505289217823e-7",
            "extra": "mean: 7.2947210274349725 usec\nrounds: 37803"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 36208.84604728223,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014236425130182326",
            "extra": "mean: 27.617560600914487 usec\nrounds: 8787"
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
          "id": "be13d3b17a6808751092e5c39d066a6bea90492c",
          "message": "Bump version to 1.8.0\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)",
          "timestamp": "2026-04-18T16:05:44+02:00",
          "tree_id": "aebdd42e3ce966bd539f0daf0eb2b369828f008e",
          "url": "https://github.com/mrijk/py-predicate/commit/be13d3b17a6808751092e5c39d066a6bea90492c"
        },
        "date": 1776521236452,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 4238107.290296149,
            "unit": "iter/sec",
            "range": "stddev: 1.7361744327486818e-7",
            "extra": "mean: 235.95438517794634 nsec\nrounds: 176960"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 6869409.96830492,
            "unit": "iter/sec",
            "range": "stddev: 3.3199253973015734e-8",
            "extra": "mean: 145.57291013550585 nsec\nrounds: 197629"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1719968.4982717233,
            "unit": "iter/sec",
            "range": "stddev: 5.813964386213537e-8",
            "extra": "mean: 581.4059972638048 nsec\nrounds: 83313"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1258763.4431155135,
            "unit": "iter/sec",
            "range": "stddev: 7.79021288377998e-8",
            "extra": "mean: 794.4304432014178 nsec\nrounds: 62500"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4415181.892594972,
            "unit": "iter/sec",
            "range": "stddev: 3.6007801325648996e-8",
            "extra": "mean: 226.49123508980998 nsec\nrounds: 195734"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7447026.7259831065,
            "unit": "iter/sec",
            "range": "stddev: 1.1986728461249329e-8",
            "extra": "mean: 134.2817793994135 nsec\nrounds: 75104"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 115782.3479245492,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011314002193247934",
            "extra": "mean: 8.636895156519547 usec\nrounds: 76371"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 64992.753376705,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013461387199904698",
            "extra": "mean: 15.386330752967062 usec\nrounds: 49218"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 62993.77508360576,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014092895042050049",
            "extra": "mean: 15.874584412075533 usec\nrounds: 44342"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1678436.3991499944,
            "unit": "iter/sec",
            "range": "stddev: 2.58363202057501e-7",
            "extra": "mean: 595.7926082313438 nsec\nrounds: 158203"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1184418.142112566,
            "unit": "iter/sec",
            "range": "stddev: 8.02505676186671e-8",
            "extra": "mean: 844.2964223904645 nsec\nrounds: 56616"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 421065.5669647338,
            "unit": "iter/sec",
            "range": "stddev: 5.821312228600283e-7",
            "extra": "mean: 2.3749270385810353 usec\nrounds: 50232"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 60209.60997130548,
            "unit": "iter/sec",
            "range": "stddev: 0.000002002513481767717",
            "extra": "mean: 16.608644375483863 usec\nrounds: 17735"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 60042.126519304395,
            "unit": "iter/sec",
            "range": "stddev: 0.000001798863268791534",
            "extra": "mean: 16.654973065927067 usec\nrounds: 27920"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1660.2825426732904,
            "unit": "iter/sec",
            "range": "stddev: 0.00003178686422837561",
            "extra": "mean: 602.3071220094009 usec\nrounds: 418"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 48091.417279926274,
            "unit": "iter/sec",
            "range": "stddev: 0.0000021286597575936935",
            "extra": "mean: 20.793731117951637 usec\nrounds: 25699"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 356560.83646683855,
            "unit": "iter/sec",
            "range": "stddev: 6.094958631396915e-7",
            "extra": "mean: 2.8045704904357986 usec\nrounds: 42637"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 6939.351730175058,
            "unit": "iter/sec",
            "range": "stddev: 0.000013644342597158147",
            "extra": "mean: 144.10568002362567 usec\nrounds: 5091"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 21963.256261042436,
            "unit": "iter/sec",
            "range": "stddev: 0.00007157545680152264",
            "extra": "mean: 45.53058927668029 usec\nrounds: 9941"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 233433.02215888503,
            "unit": "iter/sec",
            "range": "stddev: 8.265140004203649e-7",
            "extra": "mean: 4.283884048416058 usec\nrounds: 50133"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 249255.38998417222,
            "unit": "iter/sec",
            "range": "stddev: 9.169182208605019e-7",
            "extra": "mean: 4.011949350678035 usec\nrounds: 90327"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 257040.09950871993,
            "unit": "iter/sec",
            "range": "stddev: 8.034248297409539e-7",
            "extra": "mean: 3.890443560795757 usec\nrounds: 95058"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 155663.34427092216,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011187991443932779",
            "extra": "mean: 6.424119979457486 usec\nrounds: 44741"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 51003.08848315753,
            "unit": "iter/sec",
            "range": "stddev: 0.0000028701462178185893",
            "extra": "mean: 19.60665578772204 usec\nrounds: 23256"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 66634.51880372502,
            "unit": "iter/sec",
            "range": "stddev: 0.0000026063994696668354",
            "extra": "mean: 15.007236758856848 usec\nrounds: 17068"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 63378.29102799272,
            "unit": "iter/sec",
            "range": "stddev: 0.000002077635905119915",
            "extra": "mean: 15.77827334533718 usec\nrounds: 22210"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 253581.0936918038,
            "unit": "iter/sec",
            "range": "stddev: 0.000001951982904234774",
            "extra": "mean: 3.943511661067979 usec\nrounds: 77137"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 228348.61225100292,
            "unit": "iter/sec",
            "range": "stddev: 0.00000253371628046946",
            "extra": "mean: 4.379269005150733 usec\nrounds: 83872"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 277682.2729918981,
            "unit": "iter/sec",
            "range": "stddev: 7.575777836851352e-7",
            "extra": "mean: 3.6012381677283978 usec\nrounds: 47941"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 324127.23921953514,
            "unit": "iter/sec",
            "range": "stddev: 6.802968048176199e-7",
            "extra": "mean: 3.085208149762101 usec\nrounds: 68321"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 51879.201036080536,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018773025542513826",
            "extra": "mean: 19.27554742611645 usec\nrounds: 8761"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 18929.712277906303,
            "unit": "iter/sec",
            "range": "stddev: 0.000003977161496915319",
            "extra": "mean: 52.8270047277551 usec\nrounds: 11845"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 106104.71732821062,
            "unit": "iter/sec",
            "range": "stddev: 0.000001278753806892312",
            "extra": "mean: 9.424651657161757 usec\nrounds: 39375"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 120478.83976410169,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012346663093912664",
            "extra": "mean: 8.3002127341034 usec\nrounds: 34066"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 31299.860055642497,
            "unit": "iter/sec",
            "range": "stddev: 0.0000026444129211806635",
            "extra": "mean: 31.94902463532669 usec\nrounds: 6373"
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
          "id": "0e95d3132ec38a4c62c48d43d755f200588688a5",
          "message": "Improve NamedPredicate to follow standard predicate conventions (#216)\n\n- Add generic type parameter [T]\n- Fix __call__ signature from *args to typed (x: T)\n- Add @override to __call__ and __repr__\n- Add explain_failure method\n\nCo-authored-by: Maurits Rijk <maurits.rijk@surf.nl>",
          "timestamp": "2026-04-18T20:53:36+02:00",
          "tree_id": "14d3e2a64a2592ab589f7b082a370bac7c650ebb",
          "url": "https://github.com/mrijk/py-predicate/commit/0e95d3132ec38a4c62c48d43d755f200588688a5"
        },
        "date": 1776538459489,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 4792488.544900211,
            "unit": "iter/sec",
            "range": "stddev: 1.520953129175062e-7",
            "extra": "mean: 208.65986233063018 nsec\nrounds: 171851"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 6708751.065440749,
            "unit": "iter/sec",
            "range": "stddev: 2.8403651001683857e-8",
            "extra": "mean: 149.05904098176615 nsec\nrounds: 31136"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1704387.0617482807,
            "unit": "iter/sec",
            "range": "stddev: 5.6356574331048596e-8",
            "extra": "mean: 586.7211870138505 nsec\nrounds: 82796"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1218480.437666864,
            "unit": "iter/sec",
            "range": "stddev: 8.132571548650235e-8",
            "extra": "mean: 820.6943411539635 nsec\nrounds: 59756"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4210176.533490272,
            "unit": "iter/sec",
            "range": "stddev: 3.4446769934910094e-8",
            "extra": "mean: 237.51973154697896 nsec\nrounds: 195008"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7527643.168513915,
            "unit": "iter/sec",
            "range": "stddev: 1.2915708195312069e-8",
            "extra": "mean: 132.84370388101394 nsec\nrounds: 73207"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 114984.03341027455,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010956584786655692",
            "extra": "mean: 8.696859645129162 usec\nrounds: 75188"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 65758.34556077633,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013559863833529964",
            "extra": "mean: 15.207195246050745 usec\nrounds: 49727"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 62540.455630952056,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013354527186750893",
            "extra": "mean: 15.989650057891287 usec\nrounds: 44936"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1814440.613647378,
            "unit": "iter/sec",
            "range": "stddev: 2.1206079663738952e-7",
            "extra": "mean: 551.1340478594149 nsec\nrounds: 151058"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1167072.5413645033,
            "unit": "iter/sec",
            "range": "stddev: 6.971138555643345e-8",
            "extra": "mean: 856.8447671905916 nsec\nrounds: 57751"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 429954.73892397404,
            "unit": "iter/sec",
            "range": "stddev: 4.1409031752434014e-7",
            "extra": "mean: 2.3258262078995786 usec\nrounds: 43132"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 64118.43995720457,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014446760185851733",
            "extra": "mean: 15.596137408636944 usec\nrounds: 16833"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 64434.0635597278,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017964440361065793",
            "extra": "mean: 15.519741341053868 usec\nrounds: 23877"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1873.101929959449,
            "unit": "iter/sec",
            "range": "stddev: 0.000013362355915283103",
            "extra": "mean: 533.8737759037219 usec\nrounds: 415"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 52277.70791681295,
            "unit": "iter/sec",
            "range": "stddev: 0.000001850305106006964",
            "extra": "mean: 19.128612172347967 usec\nrounds: 25862"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 364486.4610499046,
            "unit": "iter/sec",
            "range": "stddev: 4.936524249299795e-7",
            "extra": "mean: 2.7435861324437028 usec\nrounds: 23162"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 7147.800156990892,
            "unit": "iter/sec",
            "range": "stddev: 0.000012186168059848232",
            "extra": "mean: 139.9031839218325 usec\nrounds: 5013"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 26296.920458621713,
            "unit": "iter/sec",
            "range": "stddev: 0.000060141763595191166",
            "extra": "mean: 38.02726640838053 usec\nrounds: 9294"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 228446.57452420238,
            "unit": "iter/sec",
            "range": "stddev: 7.18895278496862e-7",
            "extra": "mean: 4.377391090598545 usec\nrounds: 46378"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 243510.55983698982,
            "unit": "iter/sec",
            "range": "stddev: 6.843179610926251e-7",
            "extra": "mean: 4.106598090322725 usec\nrounds: 71424"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 255864.44620277244,
            "unit": "iter/sec",
            "range": "stddev: 7.048996529565749e-7",
            "extra": "mean: 3.908319482604083 usec\nrounds: 93232"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 154317.96624522604,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012710323066192904",
            "extra": "mean: 6.480126872660467 usec\nrounds: 38582"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 49737.28641909929,
            "unit": "iter/sec",
            "range": "stddev: 0.000006071400324238538",
            "extra": "mean: 20.10564049622129 usec\nrounds: 20876"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 69331.1881562924,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012857294107056265",
            "extra": "mean: 14.423523187655649 usec\nrounds: 14167"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 65723.42061906523,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013759297221309857",
            "extra": "mean: 15.215276237614406 usec\nrounds: 20200"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 253267.41966237695,
            "unit": "iter/sec",
            "range": "stddev: 7.022354019730761e-7",
            "extra": "mean: 3.948395736542305 usec\nrounds: 69099"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 226996.96840187654,
            "unit": "iter/sec",
            "range": "stddev: 8.436515903624632e-7",
            "extra": "mean: 4.405345177251862 usec\nrounds: 59468"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 275206.3009226244,
            "unit": "iter/sec",
            "range": "stddev: 6.491196526107738e-7",
            "extra": "mean: 3.633637735209976 usec\nrounds: 43413"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 320998.846272638,
            "unit": "iter/sec",
            "range": "stddev: 6.439485241514054e-7",
            "extra": "mean: 3.1152759943275847 usec\nrounds: 77161"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 51661.56824337259,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014838385593724854",
            "extra": "mean: 19.35674881740132 usec\nrounds: 8667"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 19058.22689769964,
            "unit": "iter/sec",
            "range": "stddev: 0.000003941894775935811",
            "extra": "mean: 52.47077838708605 usec\nrounds: 10577"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 106031.59856234734,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010241572562539473",
            "extra": "mean: 9.431150841435187 usec\nrounds: 33870"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 118847.58506158974,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010132250148841107",
            "extra": "mean: 8.414138154189464 usec\nrounds: 30285"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 30844.62465457874,
            "unit": "iter/sec",
            "range": "stddev: 0.000005315700731686919",
            "extra": "mean: 32.420559860875294 usec\nrounds: 7768"
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
          "id": "aa6f26b75009d613373a408f71202e8f4c3c64b1",
          "message": "Feature/async fn reduce predicates (#217)\n\n* Add async function support to fn_p and reduce_p (#194)\n\n* Resolve async check once at construction time in ReducePredicate\n\n* Resolve async check once at construction time in FnPredicate\n\n* Improve type annotations for _call field in FnPredicate and ReducePredicate\n\n---------\n\nCo-authored-by: Maurits Rijk <maurits.rijk@surf.nl>",
          "timestamp": "2026-04-19T19:34:16+02:00",
          "tree_id": "544d197941fa35d8fb1b4af1c0c0611dc10ecc42",
          "url": "https://github.com/mrijk/py-predicate/commit/aa6f26b75009d613373a408f71202e8f4c3c64b1"
        },
        "date": 1776620105277,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 8532799.300643677,
            "unit": "iter/sec",
            "range": "stddev: 2.0617750551728492e-8",
            "extra": "mean: 117.19483428194125 nsec\nrounds: 198138"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 7022384.814824409,
            "unit": "iter/sec",
            "range": "stddev: 3.999993941930037e-8",
            "extra": "mean: 142.40176611925025 nsec\nrounds: 198531"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1750705.7572834196,
            "unit": "iter/sec",
            "range": "stddev: 5.641171338965569e-8",
            "extra": "mean: 571.1982129719536 nsec\nrounds: 84246"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1223585.2894600907,
            "unit": "iter/sec",
            "range": "stddev: 9.83784642354422e-8",
            "extra": "mean: 817.2703681663677 nsec\nrounds: 61331"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4266924.96846101,
            "unit": "iter/sec",
            "range": "stddev: 3.4392697251230675e-8",
            "extra": "mean: 234.36081191759953 nsec\nrounds: 193536"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7341931.022163964,
            "unit": "iter/sec",
            "range": "stddev: 3.9111798319672234e-8",
            "extra": "mean: 136.203949203715 nsec\nrounds: 72407"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 116609.03183640284,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010550822554349713",
            "extra": "mean: 8.575665060001137 usec\nrounds: 71577"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 65045.71657773734,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016918766671728386",
            "extra": "mean: 15.373802497892102 usec\nrounds: 47640"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 63055.24528080357,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013957417510254006",
            "extra": "mean: 15.859108874237277 usec\nrounds: 44556"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1842858.9108844444,
            "unit": "iter/sec",
            "range": "stddev: 2.660349506172698e-7",
            "extra": "mean: 542.6351383134748 nsec\nrounds: 174277"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1154920.4168655288,
            "unit": "iter/sec",
            "range": "stddev: 1.09035331844095e-7",
            "extra": "mean: 865.8605263157567 nsec\nrounds: 57817"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 422838.3619291531,
            "unit": "iter/sec",
            "range": "stddev: 4.868356095552914e-7",
            "extra": "mean: 2.36496990348182 usec\nrounds: 44457"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 62148.86157249919,
            "unit": "iter/sec",
            "range": "stddev: 0.0000020101969165759507",
            "extra": "mean: 16.09039932024272 usec\nrounds: 16771"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 63427.07728823106,
            "unit": "iter/sec",
            "range": "stddev: 0.0000025333322544097376",
            "extra": "mean: 15.766137157096324 usec\nrounds: 28872"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1856.7147905626136,
            "unit": "iter/sec",
            "range": "stddev: 0.000013924908761499174",
            "extra": "mean: 538.5856810549693 usec\nrounds: 417"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 51922.7586551033,
            "unit": "iter/sec",
            "range": "stddev: 0.0000022997038587344",
            "extra": "mean: 19.259377311642773 usec\nrounds: 27794"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 359484.1023771174,
            "unit": "iter/sec",
            "range": "stddev: 5.851132376188722e-7",
            "extra": "mean: 2.781764182024796 usec\nrounds: 41884"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 7203.540655152845,
            "unit": "iter/sec",
            "range": "stddev: 0.000011991088986702671",
            "extra": "mean: 138.82062278425246 usec\nrounds: 4231"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 25768.934313513848,
            "unit": "iter/sec",
            "range": "stddev: 0.00006594256913656294",
            "extra": "mean: 38.80641658803779 usec\nrounds: 10598"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 224534.23127865948,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010405702604606141",
            "extra": "mean: 4.45366389928734 usec\nrounds: 48542"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 244261.45807955705,
            "unit": "iter/sec",
            "range": "stddev: 7.114504739975526e-7",
            "extra": "mean: 4.0939737601758495 usec\nrounds: 80717"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 251360.38652033152,
            "unit": "iter/sec",
            "range": "stddev: 7.436960399042961e-7",
            "extra": "mean: 3.978351616351903 usec\nrounds: 101989"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 153430.3301417468,
            "unit": "iter/sec",
            "range": "stddev: 8.686787636073592e-7",
            "extra": "mean: 6.517616165435797 usec\nrounds: 45121"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 52580.06128707755,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015408402393479299",
            "extra": "mean: 19.01861609746292 usec\nrounds: 23308"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 68440.84400111181,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015461820209683832",
            "extra": "mean: 14.611158214000914 usec\nrounds: 17312"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 65337.27371221634,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014139897698552057",
            "extra": "mean: 15.305199362994333 usec\nrounds: 26374"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 253497.98120392943,
            "unit": "iter/sec",
            "range": "stddev: 7.671031966051624e-7",
            "extra": "mean: 3.944804590753479 usec\nrounds: 89310"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 230622.96234436828,
            "unit": "iter/sec",
            "range": "stddev: 7.352688298527172e-7",
            "extra": "mean: 4.336081671289917 usec\nrounds: 92456"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 280242.31009963393,
            "unit": "iter/sec",
            "range": "stddev: 7.007927188811404e-7",
            "extra": "mean: 3.5683405537317765 usec\nrounds: 52444"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 322520.9666061968,
            "unit": "iter/sec",
            "range": "stddev: 6.670263380977731e-7",
            "extra": "mean: 3.10057361703562 usec\nrounds: 105553"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 52355.29954866329,
            "unit": "iter/sec",
            "range": "stddev: 0.000001921610421423299",
            "extra": "mean: 19.100263175278336 usec\nrounds: 9089"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 19104.712692292764,
            "unit": "iter/sec",
            "range": "stddev: 0.0000026114696439267866",
            "extra": "mean: 52.3431059187517 usec\nrounds: 11641"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 103415.25209435543,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012007014559739872",
            "extra": "mean: 9.669753539715847 usec\nrounds: 43930"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 120365.21885517731,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010181782634790127",
            "extra": "mean: 8.30804786890467 usec\nrounds: 29351"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 31986.33017719557,
            "unit": "iter/sec",
            "range": "stddev: 0.0000020337225877205303",
            "extra": "mean: 31.26335514140797 usec\nrounds: 7673"
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
          "id": "3321cade2eb7a929a979901fa9402d1227172010",
          "message": "Update docs and changelog for async fn_p/reduce_p support\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)",
          "timestamp": "2026-04-19T19:40:37+02:00",
          "tree_id": "9fa63768eadb122297a17da874a01f2dc4a36a62",
          "url": "https://github.com/mrijk/py-predicate/commit/3321cade2eb7a929a979901fa9402d1227172010"
        },
        "date": 1776620492523,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 4590569.875811995,
            "unit": "iter/sec",
            "range": "stddev: 1.0784826710492139e-7",
            "extra": "mean: 217.83787787853177 nsec\nrounds: 188395"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 8041841.060847174,
            "unit": "iter/sec",
            "range": "stddev: 7.848586161051366e-9",
            "extra": "mean: 124.3496349198742 nsec\nrounds: 79599"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1822940.3737310092,
            "unit": "iter/sec",
            "range": "stddev: 3.8509655302533684e-8",
            "extra": "mean: 548.5642944828204 nsec\nrounds: 90416"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1245713.7596477577,
            "unit": "iter/sec",
            "range": "stddev: 4.5889503080984866e-8",
            "extra": "mean: 802.7526325813111 nsec\nrounds: 60416"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4500290.159298596,
            "unit": "iter/sec",
            "range": "stddev: 2.0211677508797675e-8",
            "extra": "mean: 222.20789429183327 nsec\nrounds: 193649"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 8423888.525265666,
            "unit": "iter/sec",
            "range": "stddev: 8.643006892625055e-9",
            "extra": "mean: 118.71002293070619 nsec\nrounds: 82857"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 131107.98463157477,
            "unit": "iter/sec",
            "range": "stddev: 6.430249977301952e-7",
            "extra": "mean: 7.627300524907692 usec\nrounds: 81727"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 74949.15546929807,
            "unit": "iter/sec",
            "range": "stddev: 8.788710821288163e-7",
            "extra": "mean: 13.342378492972303 usec\nrounds: 55182"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 72979.12414719579,
            "unit": "iter/sec",
            "range": "stddev: 8.624666564732265e-7",
            "extra": "mean: 13.702548662862032 usec\nrounds: 49247"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 2010252.1188141687,
            "unit": "iter/sec",
            "range": "stddev: 1.422150395165285e-7",
            "extra": "mean: 497.45004153503476 nsec\nrounds: 196233"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1274302.104069723,
            "unit": "iter/sec",
            "range": "stddev: 4.236975755911422e-8",
            "extra": "mean: 784.7432699093191 nsec\nrounds: 62384"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 466962.7559900968,
            "unit": "iter/sec",
            "range": "stddev: 3.126417279267294e-7",
            "extra": "mean: 2.141498411109274 usec\nrounds: 50350"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 60830.53385772275,
            "unit": "iter/sec",
            "range": "stddev: 9.519990403756702e-7",
            "extra": "mean: 16.43911267224634 usec\nrounds: 18505"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 60789.29676880445,
            "unit": "iter/sec",
            "range": "stddev: 9.527471675545732e-7",
            "extra": "mean: 16.450264325366813 usec\nrounds: 25968"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1723.0752128586767,
            "unit": "iter/sec",
            "range": "stddev: 0.000011104878315978508",
            "extra": "mean: 580.3577188838699 usec\nrounds: 466"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 48604.009245235124,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014040927496642914",
            "extra": "mean: 20.574434404257186 usec\nrounds: 26549"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 406261.25840793026,
            "unit": "iter/sec",
            "range": "stddev: 3.72982563200697e-7",
            "extra": "mean: 2.4614702468033314 usec\nrounds: 46348"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 7600.364970158934,
            "unit": "iter/sec",
            "range": "stddev: 0.000011559540665946601",
            "extra": "mean: 131.57262893640865 usec\nrounds: 5716"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 23935.451747023737,
            "unit": "iter/sec",
            "range": "stddev: 0.0000925806109743",
            "extra": "mean: 41.77903181310732 usec\nrounds: 9933"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 266099.7319618061,
            "unit": "iter/sec",
            "range": "stddev: 6.651963524967842e-7",
            "extra": "mean: 3.757989505015858 usec\nrounds: 32587"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 279351.1730680916,
            "unit": "iter/sec",
            "range": "stddev: 4.6666265786811e-7",
            "extra": "mean: 3.5797236468244606 usec\nrounds: 81660"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 293139.62718833477,
            "unit": "iter/sec",
            "range": "stddev: 4.558407039736283e-7",
            "extra": "mean: 3.4113436303087243 usec\nrounds: 91904"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 176953.83113964493,
            "unit": "iter/sec",
            "range": "stddev: 5.642468500035106e-7",
            "extra": "mean: 5.65119157669347 usec\nrounds: 50669"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 58973.69518932235,
            "unit": "iter/sec",
            "range": "stddev: 0.000001172358950767023",
            "extra": "mean: 16.956712595161544 usec\nrounds: 24422"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 77692.03604789636,
            "unit": "iter/sec",
            "range": "stddev: 8.73292853608552e-7",
            "extra": "mean: 12.871332132208638 usec\nrounds: 17207"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 74117.84583753112,
            "unit": "iter/sec",
            "range": "stddev: 8.007061995685161e-7",
            "extra": "mean: 13.492027307323996 usec\nrounds: 17834"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 291506.45573247544,
            "unit": "iter/sec",
            "range": "stddev: 3.9784590168794077e-7",
            "extra": "mean: 3.430455759503766 usec\nrounds: 82741"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 265098.75023606385,
            "unit": "iter/sec",
            "range": "stddev: 4.268348935627216e-7",
            "extra": "mean: 3.772179231737324 usec\nrounds: 82809"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 329569.8125361866,
            "unit": "iter/sec",
            "range": "stddev: 4.070009707152141e-7",
            "extra": "mean: 3.034258484733642 usec\nrounds: 53508"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 359246.13930234854,
            "unit": "iter/sec",
            "range": "stddev: 3.985300254114239e-7",
            "extra": "mean: 2.783606810478151 usec\nrounds: 100463"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 60367.71587310131,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010426734203955044",
            "extra": "mean: 16.56514555067969 usec\nrounds: 10024"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 22292.68831756342,
            "unit": "iter/sec",
            "range": "stddev: 0.000001834227020808455",
            "extra": "mean: 44.85775720517943 usec\nrounds: 12352"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 122132.25967434807,
            "unit": "iter/sec",
            "range": "stddev: 6.418239737833584e-7",
            "extra": "mean: 8.187844904093215 usec\nrounds: 40994"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 140048.05075405366,
            "unit": "iter/sec",
            "range": "stddev: 6.81498562063811e-7",
            "extra": "mean: 7.140406414910814 usec\nrounds: 36758"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 36467.741576505796,
            "unit": "iter/sec",
            "range": "stddev: 0.0000029507833652643805",
            "extra": "mean: 27.421495183684375 usec\nrounds: 8928"
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
          "id": "971375ea04a2b4f536bed2e307665b018eaaa36d",
          "message": "Improve generate_count, generate_is_subclass, and generate_not_in gen… (#218)\n\n* Improve generate_count, generate_is_subclass, and generate_not_in generators\n\n- generate_true/false count: yield iterables with mixed true/false items;\n  false generator now uses generate_false(length_p) for correct bad counts\n- generate_true is_subclass: include class itself; unify arms via _yield_subclasses\n- generate_false is_subclass: unify arms; move warnings import to top level;\n  move Hashable import to top level\n- generate_true not_in: fix infinite-loop bug by collecting one generator per\n  unique type via dict comprehension + _generator_for_item helper\n- generate_false in: delegate to generate_true(NotInPredicate) to eliminate duplication\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)\n\n* Add generators for IsCallablePredicate and ExceptionPredicate\n\n- generate_true/false is_callable: build an annotated function via\n  generate_lambda with __annotations__ matching params and return_type\n- generate_true/false exception: yield nothing, since ExceptionPredicate\n  always raises and can never satisfy or fail a boolean check\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)\n\n* Add datetime and float support to generate_not_in; consolidate not_in tests\n\n- Add generate_datetimes and generate_floats helpers in helpers.py\n- Add datetime and float cases to _generator_for_item\n- Extract all not_in tests into test_generate_not_in.py with parametrize\n- Remove scattered not_in tests from test_generate_in.py and test_generate_true.py\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)\n\n---------\n\nCo-authored-by: Maurits Rijk <maurits.rijk@surf.nl>",
          "timestamp": "2026-05-04T15:05:27+02:00",
          "tree_id": "5d1f2c6685ec2dc233d3a3c3364a4f81c8febe99",
          "url": "https://github.com/mrijk/py-predicate/commit/971375ea04a2b4f536bed2e307665b018eaaa36d"
        },
        "date": 1777899979095,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 8002893.890261627,
            "unit": "iter/sec",
            "range": "stddev: 1.8771395208854806e-8",
            "extra": "mean: 124.9547993153897 nsec\nrounds: 196851"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 7094704.855068993,
            "unit": "iter/sec",
            "range": "stddev: 2.0556910318407435e-8",
            "extra": "mean: 140.95019037832483 nsec\nrounds: 194553"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1740405.7817162483,
            "unit": "iter/sec",
            "range": "stddev: 5.80367846889309e-8",
            "extra": "mean: 574.5786474082386 nsec\nrounds: 83669"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1286385.8692466405,
            "unit": "iter/sec",
            "range": "stddev: 7.120744856533915e-8",
            "extra": "mean: 777.3717232960903 nsec\nrounds: 60129"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4401452.305890486,
            "unit": "iter/sec",
            "range": "stddev: 3.4555972694799196e-8",
            "extra": "mean: 227.19773622485812 nsec\nrounds: 198020"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7590504.655331263,
            "unit": "iter/sec",
            "range": "stddev: 1.2586856660917697e-8",
            "extra": "mean: 131.7435461023847 nsec\nrounds: 74823"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 116285.02430757393,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011043851201513523",
            "extra": "mean: 8.599559624763028 usec\nrounds: 75908"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 64627.01731292179,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015011992307443392",
            "extra": "mean: 15.473404801555894 usec\nrounds: 48525"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 62191.73871238835,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014088231124874617",
            "extra": "mean: 16.07930604134732 usec\nrounds: 22644"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1697091.134698873,
            "unit": "iter/sec",
            "range": "stddev: 2.6056415419212913e-7",
            "extra": "mean: 589.2435471224338 nsec\nrounds: 88488"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1174932.6344732572,
            "unit": "iter/sec",
            "range": "stddev: 1.1483307299837529e-7",
            "extra": "mean: 851.1126260854243 nsec\nrounds: 57797"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 414601.8275524248,
            "unit": "iter/sec",
            "range": "stddev: 6.122933111384321e-7",
            "extra": "mean: 2.411952706295184 usec\nrounds: 47850"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 60448.64627147333,
            "unit": "iter/sec",
            "range": "stddev: 0.000001962718043219142",
            "extra": "mean: 16.542967654048454 usec\nrounds: 17962"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 61220.893510790665,
            "unit": "iter/sec",
            "range": "stddev: 0.000002313473969997212",
            "extra": "mean: 16.3342927986463 usec\nrounds: 28856"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1700.201404328651,
            "unit": "iter/sec",
            "range": "stddev: 0.00001778458587505929",
            "extra": "mean: 588.165612293953 usec\nrounds: 423"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 48790.48148025672,
            "unit": "iter/sec",
            "range": "stddev: 0.0000024008351732287166",
            "extra": "mean: 20.495801018168972 usec\nrounds: 26912"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 359168.8175174704,
            "unit": "iter/sec",
            "range": "stddev: 9.458761275751294e-7",
            "extra": "mean: 2.7842060647465834 usec\nrounds: 46927"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 6886.809547203688,
            "unit": "iter/sec",
            "range": "stddev: 0.000020457207990652578",
            "extra": "mean: 145.20511902438756 usec\nrounds: 5209"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 22214.61637234514,
            "unit": "iter/sec",
            "range": "stddev: 0.00006730668321770997",
            "extra": "mean: 45.01540711929173 usec\nrounds: 8484"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 233669.33740376332,
            "unit": "iter/sec",
            "range": "stddev: 8.450092086079319e-7",
            "extra": "mean: 4.279551656673181 usec\nrounds: 46993"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 250025.49698079674,
            "unit": "iter/sec",
            "range": "stddev: 8.750678714212814e-7",
            "extra": "mean: 3.9995920899091555 usec\nrounds: 93197"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 258272.7316945333,
            "unit": "iter/sec",
            "range": "stddev: 8.873952224451515e-7",
            "extra": "mean: 3.8718760336756315 usec\nrounds: 100011"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 153526.5904179198,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010894069352853332",
            "extra": "mean: 6.5135296581384825 usec\nrounds: 48452"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 51326.18373143397,
            "unit": "iter/sec",
            "range": "stddev: 0.000002115514454966282",
            "extra": "mean: 19.483233065457085 usec\nrounds: 23015"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 68202.03263763819,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018346871758376918",
            "extra": "mean: 14.662319601426907 usec\nrounds: 17866"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 64715.218682350656,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017852989157746108",
            "extra": "mean: 15.45231585955721 usec\nrounds: 27050"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 256412.83100229024,
            "unit": "iter/sec",
            "range": "stddev: 8.940453793921642e-7",
            "extra": "mean: 3.8999608408483586 usec\nrounds: 79726"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 235293.2990471742,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011370918846564144",
            "extra": "mean: 4.250014786011858 usec\nrounds: 80887"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 282305.11787455465,
            "unit": "iter/sec",
            "range": "stddev: 7.724155834467514e-7",
            "extra": "mean: 3.5422666352239527 usec\nrounds: 53065"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 319302.22906049324,
            "unit": "iter/sec",
            "range": "stddev: 9.072319258490246e-7",
            "extra": "mean: 3.131829060330629 usec\nrounds: 97666"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 51221.1262167088,
            "unit": "iter/sec",
            "range": "stddev: 0.0000019562094419327275",
            "extra": "mean: 19.52319431183828 usec\nrounds: 9212"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 19106.7899450573,
            "unit": "iter/sec",
            "range": "stddev: 0.000003554634700995063",
            "extra": "mean: 52.33741527883851 usec\nrounds: 11768"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 105776.65802121891,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013416012349184988",
            "extra": "mean: 9.453881590770234 usec\nrounds: 38975"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 120871.98579594395,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012224588570364937",
            "extra": "mean: 8.273215612492706 usec\nrounds: 34562"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 31715.488502636108,
            "unit": "iter/sec",
            "range": "stddev: 0.0000026697847800728767",
            "extra": "mean: 31.530335719624265 usec\nrounds: 8102"
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
          "id": "2590ce492e28dfec2ab1b4d5186f76f769ba6b0b",
          "message": "Feature/improve generators (#219)\n\n* Improve generate_count, generate_is_subclass, and generate_not_in generators\n\n- generate_true/false count: yield iterables with mixed true/false items;\n  false generator now uses generate_false(length_p) for correct bad counts\n- generate_true is_subclass: include class itself; unify arms via _yield_subclasses\n- generate_false is_subclass: unify arms; move warnings import to top level;\n  move Hashable import to top level\n- generate_true not_in: fix infinite-loop bug by collecting one generator per\n  unique type via dict comprehension + _generator_for_item helper\n- generate_false in: delegate to generate_true(NotInPredicate) to eliminate duplication\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)\n\n* Add generators for IsCallablePredicate and ExceptionPredicate\n\n- generate_true/false is_callable: build an annotated function via\n  generate_lambda with __annotations__ matching params and return_type\n- generate_true/false exception: yield nothing, since ExceptionPredicate\n  always raises and can never satisfy or fail a boolean check\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)\n\n* Add datetime and float support to generate_not_in; consolidate not_in tests\n\n- Add generate_datetimes and generate_floats helpers in helpers.py\n- Add datetime and float cases to _generator_for_item\n- Extract all not_in tests into test_generate_not_in.py with parametrize\n- Remove scattered not_in tests from test_generate_in.py and test_generate_true.py\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)\n\n* Improve explain\n\n---------\n\nCo-authored-by: Maurits Rijk <maurits.rijk@surf.nl>",
          "timestamp": "2026-05-04T15:40:21+02:00",
          "tree_id": "18c86d57b50b194d73651b6f158a587eacba37ed",
          "url": "https://github.com/mrijk/py-predicate/commit/2590ce492e28dfec2ab1b4d5186f76f769ba6b0b"
        },
        "date": 1777902072533,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 4305134.250592537,
            "unit": "iter/sec",
            "range": "stddev: 1.4791273215867427e-7",
            "extra": "mean: 232.280793534456 nsec\nrounds: 182782"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 6917892.497067892,
            "unit": "iter/sec",
            "range": "stddev: 2.078572988438085e-8",
            "extra": "mean: 144.5526943970066 nsec\nrounds: 196890"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1708445.7995217645,
            "unit": "iter/sec",
            "range": "stddev: 6.114148576954001e-8",
            "extra": "mean: 585.3273192979984 nsec\nrounds: 82967"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1276509.6321948972,
            "unit": "iter/sec",
            "range": "stddev: 1.0749793660425326e-7",
            "extra": "mean: 783.3861764760427 nsec\nrounds: 63533"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4394032.765657074,
            "unit": "iter/sec",
            "range": "stddev: 3.2969850846610525e-8",
            "extra": "mean: 227.58137076623782 nsec\nrounds: 198453"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7487660.705255112,
            "unit": "iter/sec",
            "range": "stddev: 1.1743790901201479e-8",
            "extra": "mean: 133.55306007631512 nsec\nrounds: 75387"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 116852.09264076978,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010382381123214048",
            "extra": "mean: 8.557827056415926 usec\nrounds: 73336"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 65957.4779505193,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014253760741231717",
            "extra": "mean: 15.16128316413479 usec\nrounds: 49858"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 62258.8862544821,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013630069520933309",
            "extra": "mean: 16.061964165444877 usec\nrounds: 43115"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1625160.281257063,
            "unit": "iter/sec",
            "range": "stddev: 2.730901252172251e-7",
            "extra": "mean: 615.3239231434447 nsec\nrounds: 169463"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1189132.556534559,
            "unit": "iter/sec",
            "range": "stddev: 8.129134924389605e-8",
            "extra": "mean: 840.9491393577346 nsec\nrounds: 57631"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 431451.7247669241,
            "unit": "iter/sec",
            "range": "stddev: 5.252645904759715e-7",
            "extra": "mean: 2.3177564084144366 usec\nrounds: 45954"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 61230.51042398873,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018081513575890847",
            "extra": "mean: 16.331727321486163 usec\nrounds: 18685"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 61254.89206539409,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016721632477241893",
            "extra": "mean: 16.325226708952922 usec\nrounds: 17657"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1698.5822301488909,
            "unit": "iter/sec",
            "range": "stddev: 0.000021394207959539782",
            "extra": "mean: 588.7262813954811 usec\nrounds: 430"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 49080.76851077559,
            "unit": "iter/sec",
            "range": "stddev: 0.000002252029406394644",
            "extra": "mean: 20.37457909365156 usec\nrounds: 28030"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 370600.25383674784,
            "unit": "iter/sec",
            "range": "stddev: 6.38049710727854e-7",
            "extra": "mean: 2.698325189060738 usec\nrounds: 39005"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 7075.449565432548,
            "unit": "iter/sec",
            "range": "stddev: 0.000013631275263926445",
            "extra": "mean: 141.33377543747162 usec\nrounds: 4796"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 22898.768404730195,
            "unit": "iter/sec",
            "range": "stddev: 0.00006154118993187874",
            "extra": "mean: 43.67047093211485 usec\nrounds: 10785"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 237679.1904200928,
            "unit": "iter/sec",
            "range": "stddev: 7.992620683248422e-7",
            "extra": "mean: 4.207351927749845 usec\nrounds: 50033"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 252846.53173929846,
            "unit": "iter/sec",
            "range": "stddev: 7.556509340274948e-7",
            "extra": "mean: 3.9549682296258126 usec\nrounds: 95970"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 259816.52073039318,
            "unit": "iter/sec",
            "range": "stddev: 7.558603792645074e-7",
            "extra": "mean: 3.8488699532609076 usec\nrounds: 93897"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 154381.4117640948,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010900723185677324",
            "extra": "mean: 6.477463760521036 usec\nrounds: 39846"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 49465.64017223988,
            "unit": "iter/sec",
            "range": "stddev: 0.000005478816282121906",
            "extra": "mean: 20.216052931246608 usec\nrounds: 22841"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 68830.3226627621,
            "unit": "iter/sec",
            "range": "stddev: 0.000001854877959218048",
            "extra": "mean: 14.528480491070109 usec\nrounds: 16941"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 66176.7996281782,
            "unit": "iter/sec",
            "range": "stddev: 0.000002312325535033633",
            "extra": "mean: 15.111035976635508 usec\nrounds: 26406"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 263206.7244202843,
            "unit": "iter/sec",
            "range": "stddev: 7.397033741245449e-7",
            "extra": "mean: 3.7992950301802155 usec\nrounds: 90001"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 236375.91157234216,
            "unit": "iter/sec",
            "range": "stddev: 7.775010314966784e-7",
            "extra": "mean: 4.230549523207033 usec\nrounds: 82830"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 289011.60010588035,
            "unit": "iter/sec",
            "range": "stddev: 7.252220631344324e-7",
            "extra": "mean: 3.460068729537661 usec\nrounds: 49513"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 327920.68033251766,
            "unit": "iter/sec",
            "range": "stddev: 7.353814277070428e-7",
            "extra": "mean: 3.049517947407225 usec\nrounds: 108484"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 53089.84206916117,
            "unit": "iter/sec",
            "range": "stddev: 0.0000019450042521660305",
            "extra": "mean: 18.835995004416862 usec\nrounds: 9208"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 19445.44444054965,
            "unit": "iter/sec",
            "range": "stddev: 0.000003962658094813808",
            "extra": "mean: 51.42592667692885 usec\nrounds: 11838"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 106528.50104228989,
            "unit": "iter/sec",
            "range": "stddev: 0.0000021833777426397056",
            "extra": "mean: 9.38715921294169 usec\nrounds: 41008"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 122691.53760346405,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018060572812407296",
            "extra": "mean: 8.150521376885623 usec\nrounds: 35763"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 31628.026300357276,
            "unit": "iter/sec",
            "range": "stddev: 0.00000233183552354603",
            "extra": "mean: 31.617527774368384 usec\nrounds: 8407"
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
          "id": "b91acb6df84d46740552b4e3d63ac517e1f18730",
          "message": "Async support for tee predicate (#221)\n\nCo-authored-by: Maurits Rijk <maurits.rijk@surf.nl>",
          "timestamp": "2026-05-21T08:59:45+02:00",
          "tree_id": "fe37d8e86011829e4326199106216d52505943c4",
          "url": "https://github.com/mrijk/py-predicate/commit/b91acb6df84d46740552b4e3d63ac517e1f18730"
        },
        "date": 1779346836909,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 4815888.1359683545,
            "unit": "iter/sec",
            "range": "stddev: 1.8202096211258824e-7",
            "extra": "mean: 207.64601912808445 nsec\nrounds: 198926"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 6773916.9209367,
            "unit": "iter/sec",
            "range": "stddev: 1.186730481945621e-8",
            "extra": "mean: 147.62507595999858 nsec\nrounds: 66614"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1662677.0561558097,
            "unit": "iter/sec",
            "range": "stddev: 5.813372890602913e-8",
            "extra": "mean: 601.4397061038712 nsec\nrounds: 79416"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1202985.2553108605,
            "unit": "iter/sec",
            "range": "stddev: 1.304047029490402e-7",
            "extra": "mean: 831.265383831818 nsec\nrounds: 58945"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4445833.678008191,
            "unit": "iter/sec",
            "range": "stddev: 3.2263559818712995e-8",
            "extra": "mean: 224.92969202752926 nsec\nrounds: 193125"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7650636.837424284,
            "unit": "iter/sec",
            "range": "stddev: 1.4201700142200626e-8",
            "extra": "mean: 130.7080732297139 nsec\nrounds: 75188"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 111771.62711685426,
            "unit": "iter/sec",
            "range": "stddev: 9.806041137339955e-7",
            "extra": "mean: 8.946814373155064 usec\nrounds: 69435"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 64542.78262870907,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013159170639528044",
            "extra": "mean: 15.493599117853854 usec\nrounds: 48518"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 61834.93587455659,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013026221292215308",
            "extra": "mean: 16.1720876047916 usec\nrounds: 44735"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1846035.479934122,
            "unit": "iter/sec",
            "range": "stddev: 2.1471625047798682e-7",
            "extra": "mean: 541.7013978711212 nsec\nrounds: 151516"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1158924.5450166394,
            "unit": "iter/sec",
            "range": "stddev: 7.280916972946322e-8",
            "extra": "mean: 862.8689454373774 nsec\nrounds: 56412"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 421873.1751571932,
            "unit": "iter/sec",
            "range": "stddev: 4.856257141000633e-7",
            "extra": "mean: 2.3703806235781455 usec\nrounds: 46056"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 63489.10500311749,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014507462871484008",
            "extra": "mean: 15.750733924362256 usec\nrounds: 17371"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 63280.9979952649,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013959685296431455",
            "extra": "mean: 15.802532066179275 usec\nrounds: 29673"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1868.1075323451628,
            "unit": "iter/sec",
            "range": "stddev: 0.000012812136707943738",
            "extra": "mean: 535.3010909091682 usec\nrounds: 418"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 51669.517502876675,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017769559076701461",
            "extra": "mean: 19.353770817471354 usec\nrounds: 27537"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 360168.26741810376,
            "unit": "iter/sec",
            "range": "stddev: 5.97439683440017e-7",
            "extra": "mean: 2.7764800246523196 usec\nrounds: 24330"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 7237.428867977954,
            "unit": "iter/sec",
            "range": "stddev: 0.000012023542651090997",
            "extra": "mean: 138.17061531678823 usec\nrounds: 5667"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 25832.62029901424,
            "unit": "iter/sec",
            "range": "stddev: 0.00005704788247046882",
            "extra": "mean: 38.71074588736782 usec\nrounds: 10881"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 230450.1757825213,
            "unit": "iter/sec",
            "range": "stddev: 7.062470215091814e-7",
            "extra": "mean: 4.339332771625709 usec\nrounds: 49848"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 243135.8054205843,
            "unit": "iter/sec",
            "range": "stddev: 7.156613467935813e-7",
            "extra": "mean: 4.112927745340375 usec\nrounds: 104450"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 252538.50829168083,
            "unit": "iter/sec",
            "range": "stddev: 7.407627987956349e-7",
            "extra": "mean: 3.9597921392843762 usec\nrounds: 111695"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 150273.91047774648,
            "unit": "iter/sec",
            "range": "stddev: 8.930272127454148e-7",
            "extra": "mean: 6.654515057343147 usec\nrounds: 42471"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 51212.916673297346,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015742310158690908",
            "extra": "mean: 19.526323922913857 usec\nrounds: 23768"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 68692.54555318489,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012882140884372766",
            "extra": "mean: 14.557620363999389 usec\nrounds: 17472"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 65649.5317612354,
            "unit": "iter/sec",
            "range": "stddev: 0.000001403653361587996",
            "extra": "mean: 15.232401102828247 usec\nrounds: 23757"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 250823.97302234985,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012002642553994474",
            "extra": "mean: 3.9868597405196766 usec\nrounds: 34372"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 229103.45733322477,
            "unit": "iter/sec",
            "range": "stddev: 7.115218742034909e-7",
            "extra": "mean: 4.364840284996341 usec\nrounds: 96284"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 272225.13303185994,
            "unit": "iter/sec",
            "range": "stddev: 6.572810462191454e-7",
            "extra": "mean: 3.673430108611481 usec\nrounds: 49162"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 320854.1260967265,
            "unit": "iter/sec",
            "range": "stddev: 6.581270594293573e-7",
            "extra": "mean: 3.1166811291014356 usec\nrounds: 109963"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 51370.461698320905,
            "unit": "iter/sec",
            "range": "stddev: 0.00000154464043635052",
            "extra": "mean: 19.466439797107878 usec\nrounds: 8870"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 18699.040440022327,
            "unit": "iter/sec",
            "range": "stddev: 0.000002886424687856991",
            "extra": "mean: 53.47868000005277 usec\nrounds: 11500"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 104338.88998091922,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010434105727927365",
            "extra": "mean: 9.58415409808244 usec\nrounds: 40922"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 119318.77470564867,
            "unit": "iter/sec",
            "range": "stddev: 9.585893233264642e-7",
            "extra": "mean: 8.380910736528532 usec\nrounds: 33642"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 30687.877814923588,
            "unit": "iter/sec",
            "range": "stddev: 0.0000032941293051270806",
            "extra": "mean: 32.58615685421224 usec\nrounds: 6828"
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
          "id": "af81dbcd1778c3fcb43998234196c70198ad8ddd",
          "message": "Improve construct (#222)\n\n* Prevent bool values from reaching int predicates during construct\n\n- Add predicate_accepts_value() to constructor/helpers.py: skips calling\n  a predicate when the value is clearly the wrong type, specifically\n  blocking booleans from reaching predicates with klass=int (e.g. ge_p).\n  Falls back to True (let predicate decide) for NotImplementedError klass,\n  type(Any) klass, or tuple klass (IsInstancePredicate handles its own\n  bool/int check internally).\n- Fix generate_eq false generator: use random_anys() when the eq value is\n  a bool so the false set is diverse enough to distinguish eq_p(True) from\n  semantically different predicates like ne_p(False).\n- Extract assert_generated/assert_generated_exact to test/constructor/helpers.py\n  and add test_construct_exact / test_construct_eq_exact parametrised tests.\n\n* Improve construct reliability for eq, ge, gt, le, lt predicates\n\n- Add boundary values to generate_true/generate_false for ge/gt/le/lt so\n  the false set always brackets the threshold, ruling out off-by-one\n  equivalents (e.g. gt_p(12) vs ge_p(13))\n- Add int bracketing (v±1 + interleaved random) to generate_false for\n  eq_p(int), preventing unilateral range predicates from matching\n- Yield None first in generate_false for eq_p(False) so is_falsy_p cannot\n  achieve a perfect match before mutations are tried\n- Fix gt_p and lt_p mutation handlers to use false_set instead of true_set\n- Add mutation handlers for AndPredicate, OrPredicate, XorPredicate that\n  delegate to sub-predicate mutations, fixing stuck-search when compound\n  predicates monopolise the top-20 candidate pool\n\n* Implement accepts_predicate\n\n* Filter incompatible-klass pairs from and/xor mutations in construct\n\nAdds _compatible_klasses to prevent and/xor predicate combinations\nbetween predicates that operate on disjoint types (e.g. ge_p(2) & eq_p(\"foo\")).\nOr combinations are left unrestricted since unions across types are valid.\nReplaces gray_product with itertools.permutations for cleaner pair generation.\n\n\nCo-authored-by: Maurits Rijk <maurits.rijk@surf.nl>",
          "timestamp": "2026-05-26T21:29:55+02:00",
          "tree_id": "222cfa6941a2736919bb9d0a757c79b535cd160b",
          "url": "https://github.com/mrijk/py-predicate/commit/af81dbcd1778c3fcb43998234196c70198ad8ddd"
        },
        "date": 1779823845588,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 8850491.605295897,
            "unit": "iter/sec",
            "range": "stddev: 1.1229776945269016e-8",
            "extra": "mean: 112.98807395078788 nsec\nrounds: 199243"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 7813856.216555683,
            "unit": "iter/sec",
            "range": "stddev: 1.305917338306294e-8",
            "extra": "mean: 127.97778360462283 nsec\nrounds: 194402"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1823133.6455154195,
            "unit": "iter/sec",
            "range": "stddev: 5.2107242633336516e-8",
            "extra": "mean: 548.5061407647321 nsec\nrounds: 69975"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1212015.0706270125,
            "unit": "iter/sec",
            "range": "stddev: 9.58168856783329e-8",
            "extra": "mean: 825.072248881088 nsec\nrounds: 195466"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4501982.848114143,
            "unit": "iter/sec",
            "range": "stddev: 2.1306335373656455e-8",
            "extra": "mean: 222.12434692391034 nsec\nrounds: 188822"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 8414128.314398745,
            "unit": "iter/sec",
            "range": "stddev: 9.32849286144405e-9",
            "extra": "mean: 118.84772404632123 nsec\nrounds: 83543"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 130832.68746892251,
            "unit": "iter/sec",
            "range": "stddev: 6.489286689683042e-7",
            "extra": "mean: 7.6433498336379895 usec\nrounds: 83251"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 74796.2871197298,
            "unit": "iter/sec",
            "range": "stddev: 8.71114662443553e-7",
            "extra": "mean: 13.369647592256214 usec\nrounds: 55467"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 72738.62477833578,
            "unit": "iter/sec",
            "range": "stddev: 8.501294170844673e-7",
            "extra": "mean: 13.747854087802832 usec\nrounds: 49941"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1757137.1523068848,
            "unit": "iter/sec",
            "range": "stddev: 1.6392692875922947e-7",
            "extra": "mean: 569.1075387525296 nsec\nrounds: 197473"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1273829.7481013376,
            "unit": "iter/sec",
            "range": "stddev: 5.924727811241697e-8",
            "extra": "mean: 785.0342649718418 nsec\nrounds: 61916"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 452555.7522401164,
            "unit": "iter/sec",
            "range": "stddev: 4.476035835506846e-7",
            "extra": "mean: 2.2096724990237697 usec\nrounds: 47951"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 60353.62157737476,
            "unit": "iter/sec",
            "range": "stddev: 9.970912626546667e-7",
            "extra": "mean: 16.569013985647516 usec\nrounds: 18376"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 62382.57861050595,
            "unit": "iter/sec",
            "range": "stddev: 9.170323550976475e-7",
            "extra": "mean: 16.030116456769683 usec\nrounds: 26044"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1739.35999522049,
            "unit": "iter/sec",
            "range": "stddev: 0.000013219534423964136",
            "extra": "mean: 574.9241115972861 usec\nrounds: 457"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 48428.67037358723,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015481337193277447",
            "extra": "mean: 20.648925363546535 usec\nrounds: 24961"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 396885.0068282653,
            "unit": "iter/sec",
            "range": "stddev: 3.983882694159209e-7",
            "extra": "mean: 2.5196215094935708 usec\nrounds: 49420"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 7565.012555483067,
            "unit": "iter/sec",
            "range": "stddev: 0.00001218053388379543",
            "extra": "mean: 132.18748715429524 usec\nrounds: 6111"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 23977.51113978582,
            "unit": "iter/sec",
            "range": "stddev: 0.00010619823850826276",
            "extra": "mean: 41.705746445914585 usec\nrounds: 11114"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 270796.3933270073,
            "unit": "iter/sec",
            "range": "stddev: 5.615288543555191e-7",
            "extra": "mean: 3.6928113691397053 usec\nrounds: 49520"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 283819.1993879625,
            "unit": "iter/sec",
            "range": "stddev: 4.740191627554779e-7",
            "extra": "mean: 3.523369814855494 usec\nrounds: 76203"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 294292.7113727191,
            "unit": "iter/sec",
            "range": "stddev: 5.078716255377804e-7",
            "extra": "mean: 3.3979774603847015 usec\nrounds: 90951"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 174935.29486362624,
            "unit": "iter/sec",
            "range": "stddev: 6.133998504397601e-7",
            "extra": "mean: 5.716399316556255 usec\nrounds: 44481"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 58579.78951972647,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010361113354064401",
            "extra": "mean: 17.070733920326816 usec\nrounds: 25327"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 76574.65248341051,
            "unit": "iter/sec",
            "range": "stddev: 9.96019403222536e-7",
            "extra": "mean: 13.059151658790025 usec\nrounds: 18146"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 72947.6954079986,
            "unit": "iter/sec",
            "range": "stddev: 9.92033636125494e-7",
            "extra": "mean: 13.708452260307478 usec\nrounds: 26058"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 290523.78580483596,
            "unit": "iter/sec",
            "range": "stddev: 5.912893919633329e-7",
            "extra": "mean: 3.442058959922015 usec\nrounds: 81513"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 265653.4263128206,
            "unit": "iter/sec",
            "range": "stddev: 4.622312063874349e-7",
            "extra": "mean: 3.764303039037217 usec\nrounds: 86738"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 320693.6305862556,
            "unit": "iter/sec",
            "range": "stddev: 5.163438638647608e-7",
            "extra": "mean: 3.1182409147693826 usec\nrounds: 55970"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 356448.76993827184,
            "unit": "iter/sec",
            "range": "stddev: 4.1273418901919823e-7",
            "extra": "mean: 2.805452239807632 usec\nrounds: 102397"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 60111.07130560677,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010699213581624231",
            "extra": "mean: 16.63587053566165 usec\nrounds: 9856"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 21926.35234898605,
            "unit": "iter/sec",
            "range": "stddev: 0.000003526491247040827",
            "extra": "mean: 45.60722112295361 usec\nrounds: 11826"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 121076.63174165034,
            "unit": "iter/sec",
            "range": "stddev: 7.198013390782305e-7",
            "extra": "mean: 8.259232071583968 usec\nrounds: 40341"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 137549.4169329586,
            "unit": "iter/sec",
            "range": "stddev: 7.741251603372058e-7",
            "extra": "mean: 7.270114423584935 usec\nrounds: 37099"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 36584.84227293843,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018051492366356825",
            "extra": "mean: 27.33372451190512 usec\nrounds: 7837"
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
          "id": "01f2af12a9bbd0dddd2af7fda064451539c188c0",
          "message": "Add missing __init__.py to test/constructor to fix duplicate module error\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)",
          "timestamp": "2026-05-26T21:32:42+02:00",
          "tree_id": "780a862106798452004630a317a379d9e3ba5be6",
          "url": "https://github.com/mrijk/py-predicate/commit/01f2af12a9bbd0dddd2af7fda064451539c188c0"
        },
        "date": 1779824018350,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 8019533.306065385,
            "unit": "iter/sec",
            "range": "stddev: 1.911060948298195e-8",
            "extra": "mean: 124.69553549252964 nsec\nrounds: 197239"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 7296214.283968079,
            "unit": "iter/sec",
            "range": "stddev: 2.0565124513615844e-8",
            "extra": "mean: 137.0573781251591 nsec\nrounds: 198453"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1690868.626576824,
            "unit": "iter/sec",
            "range": "stddev: 6.074977586310274e-8",
            "extra": "mean: 591.4120022585713 nsec\nrounds: 83251"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1283981.651462903,
            "unit": "iter/sec",
            "range": "stddev: 6.674846371844193e-8",
            "extra": "mean: 778.827328926898 nsec\nrounds: 62035"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4395311.741466957,
            "unit": "iter/sec",
            "range": "stddev: 3.6216717026825744e-8",
            "extra": "mean: 227.51514768921604 nsec\nrounds: 198020"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7531155.462993508,
            "unit": "iter/sec",
            "range": "stddev: 1.2194654557106076e-8",
            "extra": "mean: 132.78174974793532 nsec\nrounds: 76371"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 116150.49479218919,
            "unit": "iter/sec",
            "range": "stddev: 9.883645724758351e-7",
            "extra": "mean: 8.609519931784632 usec\nrounds: 72171"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 64629.05920937318,
            "unit": "iter/sec",
            "range": "stddev: 0.000001409361803921099",
            "extra": "mean: 15.47291593337892 usec\nrounds: 49437"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 62396.734696328225,
            "unit": "iter/sec",
            "range": "stddev: 0.000001426487197129797",
            "extra": "mean: 16.026479668636338 usec\nrounds: 43701"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1758388.74181162,
            "unit": "iter/sec",
            "range": "stddev: 2.3425941769393488e-7",
            "extra": "mean: 568.7024582344216 nsec\nrounds: 170040"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1192758.4468646224,
            "unit": "iter/sec",
            "range": "stddev: 7.726909167060076e-8",
            "extra": "mean: 838.3927211990641 nsec\nrounds: 57166"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 425006.1012774573,
            "unit": "iter/sec",
            "range": "stddev: 6.669137088223955e-7",
            "extra": "mean: 2.352907398256781 usec\nrounds: 48714"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 61620.4316140506,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017331240173466512",
            "extra": "mean: 16.22838357029589 usec\nrounds: 19136"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 63762.97086132373,
            "unit": "iter/sec",
            "range": "stddev: 0.0000019037359615877564",
            "extra": "mean: 15.683083559184709 usec\nrounds: 28782"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1760.6386530174593,
            "unit": "iter/sec",
            "range": "stddev: 0.00002549986338983036",
            "extra": "mean: 567.975716247145 usec\nrounds: 437"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 50336.15247728957,
            "unit": "iter/sec",
            "range": "stddev: 0.0000021334916832462304",
            "extra": "mean: 19.866436960019445 usec\nrounds: 27316"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 368522.3583963532,
            "unit": "iter/sec",
            "range": "stddev: 6.00672782793987e-7",
            "extra": "mean: 2.7135395647405467 usec\nrounds: 43511"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 7137.673911857911,
            "unit": "iter/sec",
            "range": "stddev: 0.00001317724231654059",
            "extra": "mean: 140.10166510110346 usec\nrounds: 4897"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 23154.264230065382,
            "unit": "iter/sec",
            "range": "stddev: 0.000060216066497930725",
            "extra": "mean: 43.18858893825349 usec\nrounds: 10378"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 237541.6169899055,
            "unit": "iter/sec",
            "range": "stddev: 9.230908809625106e-7",
            "extra": "mean: 4.209788636921234 usec\nrounds: 44284"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 252047.64505548362,
            "unit": "iter/sec",
            "range": "stddev: 8.348756857749006e-7",
            "extra": "mean: 3.967503841505317 usec\nrounds: 89679"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 262187.841588778,
            "unit": "iter/sec",
            "range": "stddev: 7.787836184350113e-7",
            "extra": "mean: 3.81405939322093 usec\nrounds: 91997"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 156001.7364682465,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010682833982332078",
            "extra": "mean: 6.410185057161501 usec\nrounds: 42241"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 51824.36205044509,
            "unit": "iter/sec",
            "range": "stddev: 0.000002255743197427162",
            "extra": "mean: 19.29594423230168 usec\nrounds: 24351"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 68824.55736058296,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016402871912663989",
            "extra": "mean: 14.529697514229387 usec\nrounds: 15971"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 65657.32091345645,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018018406695434143",
            "extra": "mean: 15.230594031061816 usec\nrounds: 23354"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 262357.3120337267,
            "unit": "iter/sec",
            "range": "stddev: 7.157623512307473e-7",
            "extra": "mean: 3.8115956908090576 usec\nrounds: 79783"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 236231.13133020888,
            "unit": "iter/sec",
            "range": "stddev: 7.355238108667858e-7",
            "extra": "mean: 4.23314232281341 usec\nrounds: 58817"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 285052.36173480866,
            "unit": "iter/sec",
            "range": "stddev: 7.338033789344826e-7",
            "extra": "mean: 3.508127397766748 usec\nrounds: 52340"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 329774.83664702333,
            "unit": "iter/sec",
            "range": "stddev: 7.047211129373305e-7",
            "extra": "mean: 3.032372057757568 usec\nrounds: 82420"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 52579.35285119859,
            "unit": "iter/sec",
            "range": "stddev: 0.0000019040814311667994",
            "extra": "mean: 19.018872347669152 usec\nrounds: 8813"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 19244.208841073483,
            "unit": "iter/sec",
            "range": "stddev: 0.0000036235875173017134",
            "extra": "mean: 51.96368467305709 usec\nrounds: 11607"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 107428.48093358478,
            "unit": "iter/sec",
            "range": "stddev: 0.000001242440856211179",
            "extra": "mean: 9.30851847954759 usec\nrounds: 30385"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 121968.16674930444,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014344852169056156",
            "extra": "mean: 8.198860626112532 usec\nrounds: 33507"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 31439.01341792947,
            "unit": "iter/sec",
            "range": "stddev: 0.000002441302242907235",
            "extra": "mean: 31.807613893815965 usec\nrounds: 7946"
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
          "id": "f280ff7ba5b176e22196a42180e5e60fbd4deb1e",
          "message": "Fix ruff import ordering in test/constructor/test_construct.py\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)",
          "timestamp": "2026-05-26T21:35:14+02:00",
          "tree_id": "c1fc9410d6d8b80bdf06300195348297c87aa3e5",
          "url": "https://github.com/mrijk/py-predicate/commit/f280ff7ba5b176e22196a42180e5e60fbd4deb1e"
        },
        "date": 1779824167769,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 4330657.925181094,
            "unit": "iter/sec",
            "range": "stddev: 1.8023611701285298e-7",
            "extra": "mean: 230.91179614658284 nsec\nrounds: 199243"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 7137054.218389275,
            "unit": "iter/sec",
            "range": "stddev: 2.0849687897061685e-8",
            "extra": "mean: 140.11382979596934 nsec\nrounds: 197278"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1663331.9637617846,
            "unit": "iter/sec",
            "range": "stddev: 5.7101649747327794e-8",
            "extra": "mean: 601.2028998338997 nsec\nrounds: 80815"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1278446.0752889642,
            "unit": "iter/sec",
            "range": "stddev: 6.77623331875328e-8",
            "extra": "mean: 782.1995931850096 nsec\nrounds: 62190"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4289433.2395578325,
            "unit": "iter/sec",
            "range": "stddev: 3.669007309937645e-8",
            "extra": "mean: 233.1310325051435 nsec\nrounds: 190877"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7487155.130057924,
            "unit": "iter/sec",
            "range": "stddev: 1.1484412177634358e-8",
            "extra": "mean: 133.5620783367238 nsec\nrounds: 75902"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 117395.03960569535,
            "unit": "iter/sec",
            "range": "stddev: 9.599573697616653e-7",
            "extra": "mean: 8.518247477566213 usec\nrounds: 79284"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 64761.75967986676,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016276782536787225",
            "extra": "mean: 15.441211062566012 usec\nrounds: 48289"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 62718.358090742135,
            "unit": "iter/sec",
            "range": "stddev: 0.000001421993027698884",
            "extra": "mean: 15.944294947153763 usec\nrounds: 45598"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1701420.8480954436,
            "unit": "iter/sec",
            "range": "stddev: 2.956174653596606e-7",
            "extra": "mean: 587.744061746623 nsec\nrounds: 173581"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1188306.3953459272,
            "unit": "iter/sec",
            "range": "stddev: 7.890151685598056e-8",
            "extra": "mean: 841.5338029960618 nsec\nrounds: 56424"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 432148.5982837299,
            "unit": "iter/sec",
            "range": "stddev: 5.852688494631935e-7",
            "extra": "mean: 2.3140188443777934 usec\nrounds: 47282"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 61564.19163203981,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017432551004445456",
            "extra": "mean: 16.24320848679138 usec\nrounds: 18759"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 63248.47771287077,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017487131568459625",
            "extra": "mean: 15.810657207272273 usec\nrounds: 29671"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1757.4503564636195,
            "unit": "iter/sec",
            "range": "stddev: 0.000023432175249726344",
            "extra": "mean: 569.0061152067033 usec\nrounds: 434"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 49731.42555181146,
            "unit": "iter/sec",
            "range": "stddev: 0.00000298332717205533",
            "extra": "mean: 20.108009953548883 usec\nrounds: 15874"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 367791.285282625,
            "unit": "iter/sec",
            "range": "stddev: 5.911061663478851e-7",
            "extra": "mean: 2.7189333733983427 usec\nrounds: 45102"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 7203.331894489629,
            "unit": "iter/sec",
            "range": "stddev: 0.000013393528629771276",
            "extra": "mean: 138.8246459620964 usec\nrounds: 5200"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 22341.429822343922,
            "unit": "iter/sec",
            "range": "stddev: 0.00007338525916766369",
            "extra": "mean: 44.759892627815994 usec\nrounds: 8410"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 239310.56762009108,
            "unit": "iter/sec",
            "range": "stddev: 7.932287600292902e-7",
            "extra": "mean: 4.178670461337563 usec\nrounds: 53320"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 254460.29029222496,
            "unit": "iter/sec",
            "range": "stddev: 9.008830204430763e-7",
            "extra": "mean: 3.9298862657571805 usec\nrounds: 94967"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 253877.78268096648,
            "unit": "iter/sec",
            "range": "stddev: 0.000002610948051524408",
            "extra": "mean: 3.938903158204442 usec\nrounds: 95878"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 157649.63478192323,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010875744656934807",
            "extra": "mean: 6.34317993431003 usec\nrounds: 44205"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 51788.79150732404,
            "unit": "iter/sec",
            "range": "stddev: 0.0000019199526092962783",
            "extra": "mean: 19.30919743239382 usec\nrounds: 23755"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 69095.86546144671,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016916333343644338",
            "extra": "mean: 14.472645987160666 usec\nrounds: 17183"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 65645.84952111462,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018017865221257826",
            "extra": "mean: 15.23325552635823 usec\nrounds: 25289"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 264787.7631433939,
            "unit": "iter/sec",
            "range": "stddev: 9.626629830769741e-7",
            "extra": "mean: 3.776609568843471 usec\nrounds: 79466"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 239629.33798250742,
            "unit": "iter/sec",
            "range": "stddev: 8.618291455672656e-7",
            "extra": "mean: 4.173111725046782 usec\nrounds: 89040"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 289982.2628470513,
            "unit": "iter/sec",
            "range": "stddev: 7.961746369327696e-7",
            "extra": "mean: 3.4484867804740236 usec\nrounds: 53519"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 331741.4768837265,
            "unit": "iter/sec",
            "range": "stddev: 7.092060536469027e-7",
            "extra": "mean: 3.0143954545379152 usec\nrounds: 95786"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 53196.866743499,
            "unit": "iter/sec",
            "range": "stddev: 0.000002133603641383228",
            "extra": "mean: 18.79809961029719 usec\nrounds: 9236"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 19422.02110646775,
            "unit": "iter/sec",
            "range": "stddev: 0.000004430293530199753",
            "extra": "mean: 51.48794734174132 usec\nrounds: 11831"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 106658.5877046621,
            "unit": "iter/sec",
            "range": "stddev: 0.0000029204952478068714",
            "extra": "mean: 9.375710118804522 usec\nrounds: 41348"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 122231.78268545197,
            "unit": "iter/sec",
            "range": "stddev: 0.000002208447449722705",
            "extra": "mean: 8.181178233924426 usec\nrounds: 33327"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 32152.787276839274,
            "unit": "iter/sec",
            "range": "stddev: 0.000002574235012669142",
            "extra": "mean: 31.10150269057182 usec\nrounds: 8176"
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
          "id": "b859dd1bf19b831ce97d5d2165334d0ef5f4ebc1",
          "message": "Add predicate decorator (#225)\n\n* Add predicate decorator\n\n* Fix ruff\n\n---------\n\nCo-authored-by: Maurits Rijk <maurits.rijk@surf.nl>",
          "timestamp": "2026-08-19T20:46:11+02:00",
          "tree_id": "ae182e863ed51e644f7765a71b5072682a74a20e",
          "url": "https://github.com/mrijk/py-predicate/commit/b859dd1bf19b831ce97d5d2165334d0ef5f4ebc1"
        },
        "date": 1787165221083,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 7903471.580004656,
            "unit": "iter/sec",
            "range": "stddev: 1.8800710395735223e-8",
            "extra": "mean: 126.52667753369855 nsec\nrounds: 196464"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 7049710.760331163,
            "unit": "iter/sec",
            "range": "stddev: 2.1491901012812726e-8",
            "extra": "mean: 141.84979128888753 nsec\nrounds: 189394"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1707919.6582141623,
            "unit": "iter/sec",
            "range": "stddev: 5.971284085712056e-8",
            "extra": "mean: 585.5076350872508 nsec\nrounds: 84020"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1302819.6052626215,
            "unit": "iter/sec",
            "range": "stddev: 7.217056756400996e-8",
            "extra": "mean: 767.5659745682294 nsec\nrounds: 64562"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4292218.415863546,
            "unit": "iter/sec",
            "range": "stddev: 3.4935293346804834e-8",
            "extra": "mean: 232.9797561801876 nsec\nrounds: 196464"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7599828.5867997855,
            "unit": "iter/sec",
            "range": "stddev: 1.2033109370319417e-8",
            "extra": "mean: 131.58191511541582 nsec\nrounds: 75844"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 122725.39177188082,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010619122360535035",
            "extra": "mean: 8.148273031051124 usec\nrounds: 79599"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 68352.79315087185,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013674102853693347",
            "extra": "mean: 14.629980047673369 usec\nrounds: 52425"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 65120.90842342055,
            "unit": "iter/sec",
            "range": "stddev: 0.000001957487789376543",
            "extra": "mean: 15.356051139488603 usec\nrounds: 47126"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1732936.4421434884,
            "unit": "iter/sec",
            "range": "stddev: 2.7600543219677724e-7",
            "extra": "mean: 577.0552085355704 nsec\nrounds: 165536"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1241819.9494537904,
            "unit": "iter/sec",
            "range": "stddev: 9.776273672308542e-8",
            "extra": "mean: 805.2697175946046 nsec\nrounds: 59064"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 425864.28548396396,
            "unit": "iter/sec",
            "range": "stddev: 5.72632709856103e-7",
            "extra": "mean: 2.348165915964454 usec\nrounds: 44402"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 62411.367644650454,
            "unit": "iter/sec",
            "range": "stddev: 0.000001814540709441049",
            "extra": "mean: 16.022722105589274 usec\nrounds: 17629"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 64038.32376024613,
            "unit": "iter/sec",
            "range": "stddev: 0.0000021682228776623846",
            "extra": "mean: 15.615649212554537 usec\nrounds: 29716"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1717.3738468686042,
            "unit": "iter/sec",
            "range": "stddev: 0.000023690019325822374",
            "extra": "mean: 582.2844000002463 usec\nrounds: 420"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 48506.34870043364,
            "unit": "iter/sec",
            "range": "stddev: 0.0000021425414423707667",
            "extra": "mean: 20.615858063772592 usec\nrounds: 26526"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 358198.3681297352,
            "unit": "iter/sec",
            "range": "stddev: 6.42333538448902e-7",
            "extra": "mean: 2.791749178594281 usec\nrounds: 45044"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 6945.956396320134,
            "unit": "iter/sec",
            "range": "stddev: 0.00001543171802370662",
            "extra": "mean: 143.96865499037472 usec\nrounds: 5681"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 21796.74866606354,
            "unit": "iter/sec",
            "range": "stddev: 0.000004439081224277052",
            "extra": "mean: 45.87840211035468 usec\nrounds: 10236"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 235091.34458464934,
            "unit": "iter/sec",
            "range": "stddev: 8.545631901673438e-7",
            "extra": "mean: 4.253665747527893 usec\nrounds: 50411"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 248861.16884903796,
            "unit": "iter/sec",
            "range": "stddev: 7.97768329119201e-7",
            "extra": "mean: 4.018304682184513 usec\nrounds: 95703"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 258104.56281360533,
            "unit": "iter/sec",
            "range": "stddev: 8.631791099557928e-7",
            "extra": "mean: 3.8743987673017903 usec\nrounds: 102052"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 151410.15671562622,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010574218798684426",
            "extra": "mean: 6.604576744994515 usec\nrounds: 45143"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 50066.08911314775,
            "unit": "iter/sec",
            "range": "stddev: 0.0000021648232779474437",
            "extra": "mean: 19.973599250782943 usec\nrounds: 23491"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 67293.27255285541,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016362303284322155",
            "extra": "mean: 14.860326479360195 usec\nrounds: 17508"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 60469.80033397869,
            "unit": "iter/sec",
            "range": "stddev: 0.000002311675068165709",
            "extra": "mean: 16.537180451678925 usec\nrounds: 133"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 257918.88584779837,
            "unit": "iter/sec",
            "range": "stddev: 7.466274500907972e-7",
            "extra": "mean: 3.8771879643979013 usec\nrounds: 86942"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 233509.9344706624,
            "unit": "iter/sec",
            "range": "stddev: 8.416525067971726e-7",
            "extra": "mean: 4.2824730445275225 usec\nrounds: 89518"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 282695.9040842005,
            "unit": "iter/sec",
            "range": "stddev: 7.681050142279144e-7",
            "extra": "mean: 3.5373699638115434 usec\nrounds: 56938"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 326093.3882962556,
            "unit": "iter/sec",
            "range": "stddev: 7.816554756437571e-7",
            "extra": "mean: 3.066606180593581 usec\nrounds: 96722"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 51729.20080598872,
            "unit": "iter/sec",
            "range": "stddev: 0.00000207403082807868",
            "extra": "mean: 19.331441128397046 usec\nrounds: 9181"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 19024.76146881913,
            "unit": "iter/sec",
            "range": "stddev: 0.000003725985586676307",
            "extra": "mean: 52.56307689528525 usec\nrounds: 11054"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 105555.09451547812,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012274654909283677",
            "extra": "mean: 9.473725589373277 usec\nrounds: 41314"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 121681.14484471484,
            "unit": "iter/sec",
            "range": "stddev: 0.000001250063785301158",
            "extra": "mean: 8.218200126865707 usec\nrounds: 37836"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 30918.64495432143,
            "unit": "iter/sec",
            "range": "stddev: 0.0000034383236600298207",
            "extra": "mean: 32.34294392517458 usec\nrounds: 6741"
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
          "id": "43767e5ef4d11854d3c5fa08db5cc73a9c03b6d1",
          "message": "Bump version",
          "timestamp": "2026-08-20T08:16:36+02:00",
          "tree_id": "3c8b6b5b33bae19ddeb960309345ef453507505b",
          "url": "https://github.com/mrijk/py-predicate/commit/43767e5ef4d11854d3c5fa08db5cc73a9c03b6d1"
        },
        "date": 1787206655788,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 5999700.406951937,
            "unit": "iter/sec",
            "range": "stddev: 1.0148221069098197e-7",
            "extra": "mean: 166.67498911133728 nsec\nrounds: 168379"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 8680139.21716498,
            "unit": "iter/sec",
            "range": "stddev: 1.3957639512725094e-8",
            "extra": "mean: 115.2055255084503 nsec\nrounds: 196928"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 2225531.70540641,
            "unit": "iter/sec",
            "range": "stddev: 4.067169694641932e-8",
            "extra": "mean: 449.3308262338988 nsec\nrounds: 106338"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1620479.1360736524,
            "unit": "iter/sec",
            "range": "stddev: 4.894192106851806e-8",
            "extra": "mean: 617.1014348404107 nsec\nrounds: 78685"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 5620053.530446034,
            "unit": "iter/sec",
            "range": "stddev: 1.3922087495317056e-8",
            "extra": "mean: 177.93424823849236 nsec\nrounds: 54093"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 9470694.741057357,
            "unit": "iter/sec",
            "range": "stddev: 8.82452739100641e-9",
            "extra": "mean: 105.58887466457979 nsec\nrounds: 90613"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 148697.256011697,
            "unit": "iter/sec",
            "range": "stddev: 7.248439135019136e-7",
            "extra": "mean: 6.725073661892838 usec\nrounds: 100554"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 85250.76261956355,
            "unit": "iter/sec",
            "range": "stddev: 9.400935999068447e-7",
            "extra": "mean: 11.73010034482105 usec\nrounds: 63800"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 83984.74581156267,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012015258932414824",
            "extra": "mean: 11.90692417220276 usec\nrounds: 61943"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 2359010.4833840313,
            "unit": "iter/sec",
            "range": "stddev: 1.950369854663052e-7",
            "extra": "mean: 423.90655193930587 nsec\nrounds: 185943"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1530698.843407346,
            "unit": "iter/sec",
            "range": "stddev: 6.132852714047399e-8",
            "extra": "mean: 653.2963713319292 nsec\nrounds: 76805"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 540328.0110906701,
            "unit": "iter/sec",
            "range": "stddev: 3.5419208537396183e-7",
            "extra": "mean: 1.8507276681463665 usec\nrounds: 51496"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 81449.02311781517,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013185963179950988",
            "extra": "mean: 12.277618094369409 usec\nrounds: 20382"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 83765.58120643959,
            "unit": "iter/sec",
            "range": "stddev: 9.977957704869992e-7",
            "extra": "mean: 11.938077496716799 usec\nrounds: 36750"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 2399.565440083689,
            "unit": "iter/sec",
            "range": "stddev: 0.000010309782575770993",
            "extra": "mean: 416.74212475952453 usec\nrounds: 521"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 66061.03200837452,
            "unit": "iter/sec",
            "range": "stddev: 0.000001446323591972386",
            "extra": "mean: 15.137517074714038 usec\nrounds: 33295"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 470676.7227666051,
            "unit": "iter/sec",
            "range": "stddev: 3.522017776962479e-7",
            "extra": "mean: 2.124600498877594 usec\nrounds: 26856"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 9367.67135347633,
            "unit": "iter/sec",
            "range": "stddev: 0.000009112296682981253",
            "extra": "mean: 106.75011561212611 usec\nrounds: 5752"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 34106.13467546206,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017102757831368002",
            "extra": "mean: 29.32023841210767 usec\nrounds: 11866"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 284558.8932500642,
            "unit": "iter/sec",
            "range": "stddev: 5.600772283364866e-7",
            "extra": "mean: 3.5142110252770116 usec\nrounds: 53368"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 311507.95321319794,
            "unit": "iter/sec",
            "range": "stddev: 5.556630381866698e-7",
            "extra": "mean: 3.210190910649379 usec\nrounds: 114640"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 324301.7293010319,
            "unit": "iter/sec",
            "range": "stddev: 5.692439522156754e-7",
            "extra": "mean: 3.0835481579308928 usec\nrounds: 129501"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 195152.68518824354,
            "unit": "iter/sec",
            "range": "stddev: 7.678557067619902e-7",
            "extra": "mean: 5.124192880233258 usec\nrounds: 49777"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 67423.15894326239,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011236149569309692",
            "extra": "mean: 14.83169901371004 usec\nrounds: 26762"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 87633.77603442418,
            "unit": "iter/sec",
            "range": "stddev: 0.00000134900906013227",
            "extra": "mean: 11.411125313226048 usec\nrounds: 20357"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 79238.46553599069,
            "unit": "iter/sec",
            "range": "stddev: 0.0000020467605350385",
            "extra": "mean: 12.620133330898398 usec\nrounds: 120"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 325233.5029518465,
            "unit": "iter/sec",
            "range": "stddev: 5.802971426832665e-7",
            "extra": "mean: 3.0747139852564884 usec\nrounds: 99355"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 294305.97212507523,
            "unit": "iter/sec",
            "range": "stddev: 5.323289669291531e-7",
            "extra": "mean: 3.397824355310793 usec\nrounds: 84261"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 351830.13321406726,
            "unit": "iter/sec",
            "range": "stddev: 5.715722140436349e-7",
            "extra": "mean: 2.842280707637855 usec\nrounds: 59578"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 418258.68104638066,
            "unit": "iter/sec",
            "range": "stddev: 5.387475958502658e-7",
            "extra": "mean: 2.390864900874849 usec\nrounds: 115567"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 68712.17049928485,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010438718376592007",
            "extra": "mean: 14.553462548682084 usec\nrounds: 8985"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 24838.368336702046,
            "unit": "iter/sec",
            "range": "stddev: 0.0000020784166946875765",
            "extra": "mean: 40.26029352831381 usec\nrounds: 12578"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 135260.74664936212,
            "unit": "iter/sec",
            "range": "stddev: 8.553092034437066e-7",
            "extra": "mean: 7.393127901269913 usec\nrounds: 34683"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 156700.86744684333,
            "unit": "iter/sec",
            "range": "stddev: 7.066252947699733e-7",
            "extra": "mean: 6.381585605065166 usec\nrounds: 33859"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 40912.448405381845,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015655084323284713",
            "extra": "mean: 24.44243840142441 usec\nrounds: 9083"
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
          "id": "988e7e87c2c107c47e0e71c351ea8853d1606163",
          "message": "Test with Python 3.15 (#228)\n\n* Test with Python 3.15\n\n* Add generators for frozenset\n\n* Add generators for frozenset\n\n* Fix mypy errors\n\nAnnotate builtin is_instance predicates so mypy can infer their types,\nand exclude the mutmut mutants directory from mypy.\n\n* Add frozendict generator and docs for is_frozendict_p\n\n* Add is_sentinel_p predicate\n\n* Add generator support for sentinel\n\n* Add is_normal_p, is_subnormal_p and is_template_p; fix generator imports on Python < 3.15\n\nThe frozendict/sentinel/template generators are only defined on newer Python\nversions, so import them inside the version checks instead of at module level.\nRequire mypy >= 2.4, which knows about the Python 3.15 builtins.\n\n* Add is_frozenset_of_p and is_frozendict_of_p predicates\n\nBoth are supported by the generators, the JSON/DOT formatters and spec\nannotations (frozenset[T], frozendict[K, V]); is_frozenset_of_p can also be compiled.\n\n* Add generator tests for sentinel, frozendict, template, normal and subnormal predicates\n\n\n* Add is_module_p predicate",
          "timestamp": "2026-10-15T08:28:52+02:00",
          "tree_id": "7af6114f97797f1bf2de93828fccc297c6b9d03b",
          "url": "https://github.com/mrijk/py-predicate/commit/988e7e87c2c107c47e0e71c351ea8853d1606163"
        },
        "date": 1792045777348,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 8606782.454706045,
            "unit": "iter/sec",
            "range": "stddev: 2.3656351030131354e-8",
            "extra": "mean: 116.18743767053351 nsec\nrounds: 194932"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 7533386.773091163,
            "unit": "iter/sec",
            "range": "stddev: 1.37963193793872e-8",
            "extra": "mean: 132.7424211872334 nsec\nrounds: 73497"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1879038.4327946096,
            "unit": "iter/sec",
            "range": "stddev: 6.135093072576336e-8",
            "extra": "mean: 532.1870923697631 nsec\nrounds: 89358"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1345509.2567163538,
            "unit": "iter/sec",
            "range": "stddev: 7.743057494534138e-8",
            "extra": "mean: 743.2130213956674 nsec\nrounds: 65665"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4571293.253506399,
            "unit": "iter/sec",
            "range": "stddev: 3.397513507842342e-8",
            "extra": "mean: 218.75647536568619 nsec\nrounds: 196890"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7841739.540173619,
            "unit": "iter/sec",
            "range": "stddev: 1.2481349188429665e-8",
            "extra": "mean: 127.52272564995951 nsec\nrounds: 76191"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 130090.05074678302,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010155584204374925",
            "extra": "mean: 7.686982934202051 usec\nrounds: 79340"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 72681.59803576501,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015730188972729463",
            "extra": "mean: 13.758640798017705 usec\nrounds: 51478"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 72198.08582802152,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013092443609632152",
            "extra": "mean: 13.850782725487164 usec\nrounds: 48036"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1691148.6336127075,
            "unit": "iter/sec",
            "range": "stddev: 2.820769315102821e-7",
            "extra": "mean: 591.3140809295722 nsec\nrounds: 163079"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1263181.2487976644,
            "unit": "iter/sec",
            "range": "stddev: 6.964724688104801e-8",
            "extra": "mean: 791.6520301040182 nsec\nrounds: 60194"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 435294.4275626087,
            "unit": "iter/sec",
            "range": "stddev: 5.045435424698843e-7",
            "extra": "mean: 2.2972956616959435 usec\nrounds: 45640"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 62775.31411677672,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016963729999813332",
            "extra": "mean: 15.929828692529789 usec\nrounds: 18639"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 64183.5142035137,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016263822839177998",
            "extra": "mean: 15.580324829662496 usec\nrounds: 27596"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1748.1891697721667,
            "unit": "iter/sec",
            "range": "stddev: 0.000017138810210826595",
            "extra": "mean: 572.0204754101785 usec\nrounds: 427"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 48965.18186213052,
            "unit": "iter/sec",
            "range": "stddev: 0.0000020687677145233456",
            "extra": "mean: 20.422675092184146 usec\nrounds: 24410"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 369411.34717659344,
            "unit": "iter/sec",
            "range": "stddev: 5.904689053900203e-7",
            "extra": "mean: 2.7070094290361904 usec\nrounds: 44225"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 7011.265880322521,
            "unit": "iter/sec",
            "range": "stddev: 0.000015761296011562254",
            "extra": "mean: 142.62759636694872 usec\nrounds: 5780"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 22009.05729916904,
            "unit": "iter/sec",
            "range": "stddev: 0.000004535792905049013",
            "extra": "mean: 45.435839727572315 usec\nrounds: 10426"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 227616.83984795335,
            "unit": "iter/sec",
            "range": "stddev: 0.000001098783873278593",
            "extra": "mean: 4.393348052226689 usec\nrounds: 24798"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 226689.5650537234,
            "unit": "iter/sec",
            "range": "stddev: 0.000001425455783059006",
            "extra": "mean: 4.411319064302801 usec\nrounds: 92251"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 253246.2734723883,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011153799243114796",
            "extra": "mean: 3.948725429553186 usec\nrounds: 96722"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 150453.60096035156,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011587327219720688",
            "extra": "mean: 6.646567404282507 usec\nrounds: 22506"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 50065.33484511293,
            "unit": "iter/sec",
            "range": "stddev: 0.000002161790461523123",
            "extra": "mean: 19.97390016652638 usec\nrounds: 24621"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 67154.54382725044,
            "unit": "iter/sec",
            "range": "stddev: 0.000002982862069461903",
            "extra": "mean: 14.89102513409097 usec\nrounds: 17347"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 59600.54298753718,
            "unit": "iter/sec",
            "range": "stddev: 0.00000211408927430328",
            "extra": "mean: 16.778370630098216 usec\nrounds: 143"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 256168.3408106264,
            "unit": "iter/sec",
            "range": "stddev: 9.29172807774065e-7",
            "extra": "mean: 3.903683011083928 usec\nrounds: 82495"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 231568.97806688122,
            "unit": "iter/sec",
            "range": "stddev: 8.846348313837506e-7",
            "extra": "mean: 4.318367720702133 usec\nrounds: 84091"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 273500.6144399807,
            "unit": "iter/sec",
            "range": "stddev: 7.244452889741557e-7",
            "extra": "mean: 3.656298915626197 usec\nrounds: 50536"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 319456.74783087464,
            "unit": "iter/sec",
            "range": "stddev: 6.976027378920335e-7",
            "extra": "mean: 3.130314218716756 usec\nrounds: 89199"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 52584.0323317398,
            "unit": "iter/sec",
            "range": "stddev: 0.0000024763849899785744",
            "extra": "mean: 19.017179848271137 usec\nrounds: 9230"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 18717.022921271353,
            "unit": "iter/sec",
            "range": "stddev: 0.0000037827455647144714",
            "extra": "mean: 53.427300068299274 usec\nrounds: 11714"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 103583.11258697895,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012495744425780692",
            "extra": "mean: 9.654083325216725 usec\nrounds: 40840"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 117224.42926054723,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012312434363550978",
            "extra": "mean: 8.530645073795702 usec\nrounds: 35382"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 30809.597194487953,
            "unit": "iter/sec",
            "range": "stddev: 0.0000024913033860672535",
            "extra": "mean: 32.45741882593995 usec\nrounds: 6831"
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
          "id": "686a0d95bc89a9cb0a0689edbf7a51e8ca1746f6",
          "message": "Bump __version__ to 1.9.0\n\n🤖 Created with help from [Claude Code](https://claude.com/claude-code)",
          "timestamp": "2026-10-15T09:35:18+02:00",
          "tree_id": "fb7c532a30a44e316d15b23792e6aaa06788868d",
          "url": "https://github.com/mrijk/py-predicate/commit/686a0d95bc89a9cb0a0689edbf7a51e8ca1746f6"
        },
        "date": 1792049766855,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 8539291.891470293,
            "unit": "iter/sec",
            "range": "stddev: 3.10082882032675e-8",
            "extra": "mean: 117.10572875473173 nsec\nrounds: 199243"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 7625003.872206774,
            "unit": "iter/sec",
            "range": "stddev: 1.4056792405651726e-8",
            "extra": "mean: 131.14747438293264 nsec\nrounds: 74267"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1865075.7899562584,
            "unit": "iter/sec",
            "range": "stddev: 6.456544884352432e-8",
            "extra": "mean: 536.1712405389451 nsec\nrounds: 89840"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1327486.3804353406,
            "unit": "iter/sec",
            "range": "stddev: 6.8494640304509e-8",
            "extra": "mean: 753.3033971106026 nsec\nrounds: 64025"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4549479.086397989,
            "unit": "iter/sec",
            "range": "stddev: 3.224801817350194e-8",
            "extra": "mean: 219.80538453068078 nsec\nrounds: 194932"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7838276.192209911,
            "unit": "iter/sec",
            "range": "stddev: 1.3301702838324062e-8",
            "extra": "mean: 127.5790716578541 nsec\nrounds: 77256"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 131844.62902498437,
            "unit": "iter/sec",
            "range": "stddev: 9.232061010066307e-7",
            "extra": "mean: 7.584685150962816 usec\nrounds: 81150"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 73083.11799124833,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017039386952209307",
            "extra": "mean: 13.683050579748793 usec\nrounds: 51661"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 71308.49973053011,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014481906485026354",
            "extra": "mean: 14.023573680261553 usec\nrounds: 47964"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1719293.0355180127,
            "unit": "iter/sec",
            "range": "stddev: 2.726318564741795e-7",
            "extra": "mean: 581.6344156240393 nsec\nrounds: 150083"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1291737.3746631977,
            "unit": "iter/sec",
            "range": "stddev: 6.6870183105281e-8",
            "extra": "mean: 774.151170055551 nsec\nrounds: 59698"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 432060.6346958252,
            "unit": "iter/sec",
            "range": "stddev: 5.693301426489349e-7",
            "extra": "mean: 2.314489957420003 usec\nrounds: 46751"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 62565.38524749515,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018084607305320449",
            "extra": "mean: 15.983278869685146 usec\nrounds: 12669"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 63613.95907940792,
            "unit": "iter/sec",
            "range": "stddev: 0.000001739529552582682",
            "extra": "mean: 15.719820216687376 usec\nrounds: 27967"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1713.8577746601077,
            "unit": "iter/sec",
            "range": "stddev: 0.00004952293854457785",
            "extra": "mean: 583.4789880381527 usec\nrounds: 418"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 48854.362619731386,
            "unit": "iter/sec",
            "range": "stddev: 0.000002375945855564097",
            "extra": "mean: 20.46900105490514 usec\nrounds: 25594"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 365818.3111017029,
            "unit": "iter/sec",
            "range": "stddev: 7.056729837792007e-7",
            "extra": "mean: 2.7335974434641828 usec\nrounds: 20653"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 6969.15267935134,
            "unit": "iter/sec",
            "range": "stddev: 0.000023188451228343124",
            "extra": "mean: 143.4894665118853 usec\nrounds: 5166"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 21760.902358571046,
            "unit": "iter/sec",
            "range": "stddev: 0.000005088149184327901",
            "extra": "mean: 45.953976701987564 usec\nrounds: 10473"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 227311.35970318608,
            "unit": "iter/sec",
            "range": "stddev: 8.303908351588917e-7",
            "extra": "mean: 4.399252203258822 usec\nrounds: 48905"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 241261.06882108428,
            "unit": "iter/sec",
            "range": "stddev: 0.000001481770360073691",
            "extra": "mean: 4.14488754810908 usec\nrounds: 90910"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 237474.4004535437,
            "unit": "iter/sec",
            "range": "stddev: 0.000008960738145963397",
            "extra": "mean: 4.210980207088159 usec\nrounds: 88567"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 152114.63969713726,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012255250854269853",
            "extra": "mean: 6.573989209658034 usec\nrounds: 32251"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 50995.92702125334,
            "unit": "iter/sec",
            "range": "stddev: 0.0000024728466374443314",
            "extra": "mean: 19.609409190330723 usec\nrounds: 22415"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 66846.78299546948,
            "unit": "iter/sec",
            "range": "stddev: 0.0000019521232559726404",
            "extra": "mean: 14.959583022383812 usec\nrounds: 17423"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 59637.51074838525,
            "unit": "iter/sec",
            "range": "stddev: 0.000003159348743365694",
            "extra": "mean: 16.76797014917455 usec\nrounds: 134"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 248153.95433973774,
            "unit": "iter/sec",
            "range": "stddev: 8.127967029573609e-7",
            "extra": "mean: 4.029756457682474 usec\nrounds: 84589"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 216802.30081133384,
            "unit": "iter/sec",
            "range": "stddev: 0.000002104602893005473",
            "extra": "mean: 4.612497174881101 usec\nrounds: 74157"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 276958.9008015536,
            "unit": "iter/sec",
            "range": "stddev: 7.88944851818159e-7",
            "extra": "mean: 3.610644023737368 usec\nrounds: 54189"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 324082.2052886393,
            "unit": "iter/sec",
            "range": "stddev: 7.055236317728365e-7",
            "extra": "mean: 3.0856368652186994 usec\nrounds: 87177"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 50766.86755691207,
            "unit": "iter/sec",
            "range": "stddev: 0.0000023381751802571673",
            "extra": "mean: 19.69788659658689 usec\nrounds: 8192"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 19011.14139740492,
            "unit": "iter/sec",
            "range": "stddev: 0.000004510404268823268",
            "extra": "mean: 52.60073443757054 usec\nrounds: 7727"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 104842.27979379696,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016533577830166808",
            "extra": "mean: 9.538136732306782 usec\nrounds: 40071"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 120447.56108887983,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012784794490122411",
            "extra": "mean: 8.302368192097196 usec\nrounds: 33105"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 30858.80508015087,
            "unit": "iter/sec",
            "range": "stddev: 0.000003470946915192561",
            "extra": "mean: 32.405661768258945 usec\nrounds: 8166"
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
          "id": "7c1ad9697bb987955114bea7463b04cb94edf5fc",
          "message": "Use TypeIs for is_none_p to narrow both branches (#232)",
          "timestamp": "2026-10-15T10:36:27+02:00",
          "tree_id": "19e5064810c77fee0360ec2a40aa2577c992d5af",
          "url": "https://github.com/mrijk/py-predicate/commit/7c1ad9697bb987955114bea7463b04cb94edf5fc"
        },
        "date": 1792053434539,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 8727204.702852651,
            "unit": "iter/sec",
            "range": "stddev: 1.3218470042635646e-8",
            "extra": "mean: 114.58422645605312 nsec\nrounds: 86498"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 7490802.490487925,
            "unit": "iter/sec",
            "range": "stddev: 1.9480820322383846e-8",
            "extra": "mean: 133.4970453792947 nsec\nrounds: 75387"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1793167.6385357066,
            "unit": "iter/sec",
            "range": "stddev: 5.768136452389634e-8",
            "extra": "mean: 557.6723439067839 nsec\nrounds: 86791"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1327823.8899592145,
            "unit": "iter/sec",
            "range": "stddev: 7.09084156884617e-8",
            "extra": "mean: 753.1119206107339 nsec\nrounds: 65198"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4546109.232976316,
            "unit": "iter/sec",
            "range": "stddev: 3.2171710300246987e-8",
            "extra": "mean: 219.9683176871896 nsec\nrounds: 194175"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7905798.781037284,
            "unit": "iter/sec",
            "range": "stddev: 1.1876488554377912e-8",
            "extra": "mean: 126.48943233902983 nsec\nrounds: 76366"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 131535.91933628806,
            "unit": "iter/sec",
            "range": "stddev: 9.623567006011206e-7",
            "extra": "mean: 7.602486112127098 usec\nrounds: 81150"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 72176.73601224847,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012672453055659237",
            "extra": "mean: 13.854879774977617 usec\nrounds: 52618"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 68386.54543486747,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014956296588242106",
            "extra": "mean: 14.622759398665886 usec\nrounds: 45166"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1664021.8158908314,
            "unit": "iter/sec",
            "range": "stddev: 2.836850391850789e-7",
            "extra": "mean: 600.9536596517826 nsec\nrounds: 172981"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1120366.5710900777,
            "unit": "iter/sec",
            "range": "stddev: 2.734693039119436e-7",
            "extra": "mean: 892.5650102421699 nsec\nrounds: 59556"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 435856.3206614123,
            "unit": "iter/sec",
            "range": "stddev: 5.668020803457081e-7",
            "extra": "mean: 2.2943340559625227 usec\nrounds: 40592"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 63092.987236453984,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017524533322486311",
            "extra": "mean: 15.849622023003821 usec\nrounds: 18181"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 64148.24124616034,
            "unit": "iter/sec",
            "range": "stddev: 0.00000277597731127817",
            "extra": "mean: 15.58889192554217 usec\nrounds: 28101"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1762.9079148563433,
            "unit": "iter/sec",
            "range": "stddev: 0.000015996618507908607",
            "extra": "mean: 567.2446028364951 usec\nrounds: 423"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 49984.98863821437,
            "unit": "iter/sec",
            "range": "stddev: 0.0000022696061199907453",
            "extra": "mean: 20.006006347983504 usec\nrounds: 26150"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 365325.687652623,
            "unit": "iter/sec",
            "range": "stddev: 8.445490150820203e-7",
            "extra": "mean: 2.7372835631281136 usec\nrounds: 47217"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 7189.053360659994,
            "unit": "iter/sec",
            "range": "stddev: 0.000013332938795444802",
            "extra": "mean: 139.10037244572553 usec\nrounds: 4747"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 22632.292973443575,
            "unit": "iter/sec",
            "range": "stddev: 0.000006409008804847295",
            "extra": "mean: 44.18465248631177 usec\nrounds: 10578"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 235219.559847133,
            "unit": "iter/sec",
            "range": "stddev: 8.199948108993415e-7",
            "extra": "mean: 4.251347127126207 usec\nrounds: 47461"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 247930.8359782178,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010009010462726961",
            "extra": "mean: 4.0333829233240515 usec\nrounds: 84876"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 255663.37092687248,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018944938406556566",
            "extra": "mean: 3.911393315259191 usec\nrounds: 80691"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 155916.98379737465,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010665789749197874",
            "extra": "mean: 6.413669477467394 usec\nrounds: 39846"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 51940.291309679975,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018970599371963503",
            "extra": "mean: 19.252876231243484 usec\nrounds: 23148"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 68322.82298162756,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016325660249919555",
            "extra": "mean: 14.636397566138426 usec\nrounds: 17914"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 62642.665495966394,
            "unit": "iter/sec",
            "range": "stddev: 0.00000249203377375189",
            "extra": "mean: 15.963560810872435 usec\nrounds: 148"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 255408.59037768914,
            "unit": "iter/sec",
            "range": "stddev: 7.326557216945507e-7",
            "extra": "mean: 3.9152950905889092 usec\nrounds: 81680"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 228892.0527081909,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010121494510916146",
            "extra": "mean: 4.368871650056267 usec\nrounds: 76307"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 284828.49325677933,
            "unit": "iter/sec",
            "range": "stddev: 7.636921373221321e-7",
            "extra": "mean: 3.510884703162325 usec\nrounds: 53462"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 311795.1658407338,
            "unit": "iter/sec",
            "range": "stddev: 0.0000025693976723638243",
            "extra": "mean: 3.2072338174441226 usec\nrounds: 94608"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 52918.6085187647,
            "unit": "iter/sec",
            "range": "stddev: 0.0000021312550657536753",
            "extra": "mean: 18.896944345114527 usec\nrounds: 8948"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 19182.96422336608,
            "unit": "iter/sec",
            "range": "stddev: 0.0000047809281243687",
            "extra": "mean: 52.12958687489683 usec\nrounds: 11718"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 106386.70857504127,
            "unit": "iter/sec",
            "range": "stddev: 0.000001343466800349135",
            "extra": "mean: 9.399670441863861 usec\nrounds: 40263"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 120078.92028633246,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012752808174939414",
            "extra": "mean: 8.32785635992949 usec\nrounds: 33939"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 30729.919700175284,
            "unit": "iter/sec",
            "range": "stddev: 0.000002676864552023061",
            "extra": "mean: 32.5415754338693 usec\nrounds: 7954"
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
          "id": "669451f80f46064e5f4b2dfd14fc2dc663346eca",
          "message": "Share checks between __call__ and explain_failure (#233)\n\n* Share checks between __call__ and explain_failure\n\nExtract shared failure generators in dict_of, struct and exactly predicates.\nFix struct_p skipping falsy optional values and not explaining optional failures.\n\n* Fix is_callable_p explain crash on parameter count mismatch",
          "timestamp": "2026-10-15T19:39:54+02:00",
          "tree_id": "ca96f7209cd3ba9b04b777e7702f7c3b3a5438ae",
          "url": "https://github.com/mrijk/py-predicate/commit/669451f80f46064e5f4b2dfd14fc2dc663346eca"
        },
        "date": 1792086041978,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 11949110.411780994,
            "unit": "iter/sec",
            "range": "stddev: 8.589623106545328e-9",
            "extra": "mean: 83.68823833229202 nsec\nrounds: 112297"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 10805640.93698361,
            "unit": "iter/sec",
            "range": "stddev: 5.9243993343227376e-9",
            "extra": "mean: 92.54425589669368 nsec\nrounds: 52869"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 2643348.671337402,
            "unit": "iter/sec",
            "range": "stddev: 4.718445363458052e-8",
            "extra": "mean: 378.3080192345757 nsec\nrounds: 119575"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1862505.4138801785,
            "unit": "iter/sec",
            "range": "stddev: 4.313162465561624e-8",
            "extra": "mean: 536.9111909944405 nsec\nrounds: 88254"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 6233495.085894129,
            "unit": "iter/sec",
            "range": "stddev: 1.0100682417100227e-8",
            "extra": "mean: 160.42364455583115 nsec\nrounds: 61478"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 11215275.911360838,
            "unit": "iter/sec",
            "range": "stddev: 7.062882527698412e-9",
            "extra": "mean: 89.16410152576105 nsec\nrounds: 109135"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 181041.3654442521,
            "unit": "iter/sec",
            "range": "stddev: 5.898678818649463e-7",
            "extra": "mean: 5.523599524043189 usec\nrounds: 104211"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 100870.5137163094,
            "unit": "iter/sec",
            "range": "stddev: 8.275956059215787e-7",
            "extra": "mean: 9.913699882727112 usec\nrounds: 67377"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 96487.5726526861,
            "unit": "iter/sec",
            "range": "stddev: 9.809346362407059e-7",
            "extra": "mean: 10.364028988474725 usec\nrounds: 59127"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 2472383.0178079633,
            "unit": "iter/sec",
            "range": "stddev: 1.4314320228736105e-7",
            "extra": "mean: 404.4680750503653 nsec\nrounds: 179405"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1846883.161913048,
            "unit": "iter/sec",
            "range": "stddev: 4.925123981671076e-8",
            "extra": "mean: 541.4527678969009 nsec\nrounds: 87720"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 553805.6585354188,
            "unit": "iter/sec",
            "range": "stddev: 4.048318884214171e-7",
            "extra": "mean: 1.8056875811716624 usec\nrounds: 50061"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 85545.80446704163,
            "unit": "iter/sec",
            "range": "stddev: 0.00000121500965153263",
            "extra": "mean: 11.689644001013185 usec\nrounds: 19795"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 87605.18740887317,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011479502907709136",
            "extra": "mean: 11.414849161075066 usec\nrounds: 30874"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 2490.7207351522857,
            "unit": "iter/sec",
            "range": "stddev: 0.000014389893631205974",
            "extra": "mean: 401.4902136103423 usec\nrounds: 529"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 64546.572989567525,
            "unit": "iter/sec",
            "range": "stddev: 0.000001465939883947386",
            "extra": "mean: 15.492689289044472 usec\nrounds: 31547"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 481705.90303380345,
            "unit": "iter/sec",
            "range": "stddev: 4.2862206683725783e-7",
            "extra": "mean: 2.0759554610021573 usec\nrounds: 51685"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 9749.178388369424,
            "unit": "iter/sec",
            "range": "stddev: 0.000009272865440540567",
            "extra": "mean: 102.57274614986841 usec\nrounds: 7792"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 32563.74192271254,
            "unit": "iter/sec",
            "range": "stddev: 0.000002854991147507514",
            "extra": "mean: 30.709001513813142 usec\nrounds: 12551"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 324496.17482042516,
            "unit": "iter/sec",
            "range": "stddev: 5.326065290912947e-7",
            "extra": "mean: 3.0817004254469125 usec\nrounds: 48422"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 339744.0211617727,
            "unit": "iter/sec",
            "range": "stddev: 4.694179182122229e-7",
            "extra": "mean: 2.9433924887933185 usec\nrounds: 104910"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 355644.7099996592,
            "unit": "iter/sec",
            "range": "stddev: 5.335743172394983e-7",
            "extra": "mean: 2.8117949512055396 usec\nrounds: 101410"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 212710.55430321893,
            "unit": "iter/sec",
            "range": "stddev: 6.00387345756092e-7",
            "extra": "mean: 4.701224174210462 usec\nrounds: 47985"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 70509.47888571763,
            "unit": "iter/sec",
            "range": "stddev: 0.000001545213078131791",
            "extra": "mean: 14.18249029496883 usec\nrounds: 27563"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 93836.08475806698,
            "unit": "iter/sec",
            "range": "stddev: 0.000001240561627770414",
            "extra": "mean: 10.656881119648709 usec\nrounds: 19793"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 82659.25521126464,
            "unit": "iter/sec",
            "range": "stddev: 0.000002085991748790501",
            "extra": "mean: 12.097858823481415 usec\nrounds: 85"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 350643.64997980214,
            "unit": "iter/sec",
            "range": "stddev: 5.191129242117942e-7",
            "extra": "mean: 2.8518982164873146 usec\nrounds: 100645"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 320132.22227960546,
            "unit": "iter/sec",
            "range": "stddev: 4.860495954311763e-7",
            "extra": "mean: 3.123709300110983 usec\nrounds: 94644"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 388994.11677406565,
            "unit": "iter/sec",
            "range": "stddev: 4.3817012813752803e-7",
            "extra": "mean: 2.570732967102474 usec\nrounds: 55525"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 437731.2029904199,
            "unit": "iter/sec",
            "range": "stddev: 4.7109344176496086e-7",
            "extra": "mean: 2.2845070060538633 usec\nrounds: 112474"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 70676.71904455083,
            "unit": "iter/sec",
            "range": "stddev: 0.0000028263502165341614",
            "extra": "mean: 14.14893070191407 usec\nrounds: 9957"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 26520.451738110296,
            "unit": "iter/sec",
            "range": "stddev: 0.000004354286751990057",
            "extra": "mean: 37.70674835689109 usec\nrounds: 14759"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 145935.3153190929,
            "unit": "iter/sec",
            "range": "stddev: 8.001660685404949e-7",
            "extra": "mean: 6.852350973535526 usec\nrounds: 46428"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 167256.41201452192,
            "unit": "iter/sec",
            "range": "stddev: 7.279314294553065e-7",
            "extra": "mean: 5.9788440272961 usec\nrounds: 40116"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 43572.933268875764,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016733817866712627",
            "extra": "mean: 22.950027114982 usec\nrounds: 9220"
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
          "id": "6d5cf73a3756bb8c9c7c03a9cdbf2d74a6f02d56",
          "message": "Split And/Or/Xor/Not predicates into their own files (#234)\n\nMove AndPredicate, OrPredicate, XorPredicate and NotPredicate (plus\nand_p/or_p/xor_p) out of predicate.py, using local imports in the\noperator methods to break the import cycle. Also make explain final,\nmake x positional-only in explain_failure, and require Python >= 3.12.",
          "timestamp": "2026-10-15T20:36:12+02:00",
          "tree_id": "2d0662bb6d5adb5decc9a0fba9138fd32b54c1d6",
          "url": "https://github.com/mrijk/py-predicate/commit/6d5cf73a3756bb8c9c7c03a9cdbf2d74a6f02d56"
        },
        "date": 1792089414690,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 8378163.521769781,
            "unit": "iter/sec",
            "range": "stddev: 2.91778099528105e-8",
            "extra": "mean: 119.3578995446442 nsec\nrounds: 84296"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 3973432.6683868417,
            "unit": "iter/sec",
            "range": "stddev: 2.3328810819607895e-7",
            "extra": "mean: 251.67156045102584 nsec\nrounds: 199641"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1431140.4426016363,
            "unit": "iter/sec",
            "range": "stddev: 3.044072130508354e-7",
            "extra": "mean: 698.7434428043441 nsec\nrounds: 192308"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1330547.6887685533,
            "unit": "iter/sec",
            "range": "stddev: 1.025800568542116e-7",
            "extra": "mean: 751.570205593697 nsec\nrounds: 65712"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4519137.402224077,
            "unit": "iter/sec",
            "range": "stddev: 3.0588386237913826e-8",
            "extra": "mean: 221.28116739886104 nsec\nrounds: 40790"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7994458.883504433,
            "unit": "iter/sec",
            "range": "stddev: 1.2002473014396722e-8",
            "extra": "mean: 125.08663995550407 nsec\nrounds: 77496"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 131101.6684553268,
            "unit": "iter/sec",
            "range": "stddev: 9.680011065588315e-7",
            "extra": "mean: 7.62766799066903 usec\nrounds: 71501"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 73103.80666555569,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013428068841118137",
            "extra": "mean: 13.679178220840445 usec\nrounds: 49001"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 71288.75423907992,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012997647252675255",
            "extra": "mean: 14.027457916382106 usec\nrounds: 39374"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1719935.7436549736,
            "unit": "iter/sec",
            "range": "stddev: 2.396591959622577e-7",
            "extra": "mean: 581.4170696138542 nsec\nrounds: 101338"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1309604.594662222,
            "unit": "iter/sec",
            "range": "stddev: 6.63507568868466e-8",
            "extra": "mean: 763.5892574566933 nsec\nrounds: 61047"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 432525.05945692334,
            "unit": "iter/sec",
            "range": "stddev: 5.07655195650999e-7",
            "extra": "mean: 2.312004768592127 usec\nrounds: 30827"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 62787.37324725129,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017945464818984956",
            "extra": "mean: 15.926769162042913 usec\nrounds: 10085"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 64950.01331124364,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016112307109130949",
            "extra": "mean: 15.396455659030448 usec\nrounds: 25879"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1744.018449051322,
            "unit": "iter/sec",
            "range": "stddev: 0.000015233549319484336",
            "extra": "mean: 573.3884297749034 usec\nrounds: 356"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 48889.07073855994,
            "unit": "iter/sec",
            "range": "stddev: 0.000002038080354961249",
            "extra": "mean: 20.45446937103014 usec\nrounds: 25613"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 364176.5891193116,
            "unit": "iter/sec",
            "range": "stddev: 6.227709723782303e-7",
            "extra": "mean: 2.7459206052160035 usec\nrounds: 29939"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 7065.06395197939,
            "unit": "iter/sec",
            "range": "stddev: 0.000012737330789623375",
            "extra": "mean: 141.5415354760991 usec\nrounds: 4947"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 22425.959310376562,
            "unit": "iter/sec",
            "range": "stddev: 0.0000036928594058091344",
            "extra": "mean: 44.591180522533854 usec\nrounds: 8841"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 229812.71290912104,
            "unit": "iter/sec",
            "range": "stddev: 0.000001577234579870447",
            "extra": "mean: 4.351369370916603 usec\nrounds: 34020"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 243481.48731588913,
            "unit": "iter/sec",
            "range": "stddev: 7.646752216024272e-7",
            "extra": "mean: 4.107088432159179 usec\nrounds: 93371"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 238352.1541050799,
            "unit": "iter/sec",
            "range": "stddev: 8.389243123313927e-7",
            "extra": "mean: 4.195472886555664 usec\nrounds: 84589"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 147213.37555353783,
            "unit": "iter/sec",
            "range": "stddev: 9.775115453970124e-7",
            "extra": "mean: 6.792861017145313 usec\nrounds: 33997"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 49030.254576506515,
            "unit": "iter/sec",
            "range": "stddev: 0.0000022441501158175",
            "extra": "mean: 20.395570217560383 usec\nrounds: 17695"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 66318.8282118696,
            "unit": "iter/sec",
            "range": "stddev: 0.000002101201077891972",
            "extra": "mean: 15.078674140702358 usec\nrounds: 14896"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 60303.97361629452,
            "unit": "iter/sec",
            "range": "stddev: 0.000003216383740511119",
            "extra": "mean: 16.582655172325055 usec\nrounds: 116"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 259364.8055191411,
            "unit": "iter/sec",
            "range": "stddev: 8.27690703420253e-7",
            "extra": "mean: 3.8555732262841653 usec\nrounds: 76605"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 239155.92887674485,
            "unit": "iter/sec",
            "range": "stddev: 0.000001053006709548539",
            "extra": "mean: 4.181372398738965 usec\nrounds: 81018"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 266730.86010403716,
            "unit": "iter/sec",
            "range": "stddev: 7.468855689821283e-7",
            "extra": "mean: 3.7490974970423547 usec\nrounds: 34719"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 317596.4962441559,
            "unit": "iter/sec",
            "range": "stddev: 7.020974856570843e-7",
            "extra": "mean: 3.1486493453984408 usec\nrounds: 91660"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 50727.91557210011,
            "unit": "iter/sec",
            "range": "stddev: 0.000001816942174307902",
            "extra": "mean: 19.713011834257014 usec\nrounds: 7605"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 18354.83521821842,
            "unit": "iter/sec",
            "range": "stddev: 0.00000408773573666084",
            "extra": "mean: 54.48155693642142 usec\nrounds: 10380"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 103599.78650618094,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018366332418513241",
            "extra": "mean: 9.652529543971003 usec\nrounds: 31597"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 117765.47808164009,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011860278346448018",
            "extra": "mean: 8.49145281189074 usec\nrounds: 30940"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 31177.10811043534,
            "unit": "iter/sec",
            "range": "stddev: 0.0000026251878741570354",
            "extra": "mean: 32.07481580580876 usec\nrounds: 4821"
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
          "id": "6e23f105c00a5cc4ce38b63a4124cefa89b82412",
          "message": "Same signature predicate (#235)\n\n* Add same_signatur_predicate\n\n* Fix same_signature_p checks and add explain_failure\n\n- Treat None annotation as NoneType\n- Split the child union before the superclass union\n- Check parameter types contravariantly\n- Only drop extra parameters with defaults\n- Share checks between __call__ and explain_failure\n\n* Reuse is_subclass_p in same_signature_p\n\n- is_subclass_p accepts None and union values, and returns False for non-classes\n- Replace is_subclass_safe with is_subclass_p, which also handles ABCs\n- Add type annotations to remove_default_args\n\n* Add repr to same_signature_p and fix mypy errors\n\n- Add __repr__ to SameSignaturePredicate\n- Annotate protocol as type, since Protocol is not valid as a type\n- Use ... bodies in same_signature tests and disable empty-body there\n\n* Explain parameter types and allow reordered keyword-only args\n\n- Show actual and expected type for incompatible parameters\n- Compare keyword-only parameters by name, not position\n\n* Handle more annotation and parameter cases in same_signature_p\n\n- Evaluate string annotations\n- Allow extra *args and **kwargs in the candidate function\n- Treat Any and missing annotations as compatible with every type\n- Ignore type arguments of generics such as list[int]\n\n* Check parameter kinds and defaults in same_signature_p\n\n- Reject positional-only or keyword-only where f accepts both\n- Reject a missing default where f has one\n\n* Add documentation for same_signature_p\n\n* Handle non-callables and positional-only names in same_signature_p\n\n- Return False for non-callables and builtins without a signature\n- Ignore the names of positional-only parameters in f\n- Add tests for substitutes that should be accepted\n\n* Return the first failure instead of yielding in same_signature_p\n\nThe return after each yield was never reached, since only the first\nfailure is used.",
          "timestamp": "2026-10-15T22:44:57+02:00",
          "tree_id": "2855a28b36fe09adc021fa057929bc8b84565c49",
          "url": "https://github.com/mrijk/py-predicate/commit/6e23f105c00a5cc4ce38b63a4124cefa89b82412"
        },
        "date": 1792097148453,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 6642517.696904013,
            "unit": "iter/sec",
            "range": "stddev: 1.8468615900111504e-8",
            "extra": "mean: 150.54532718310807 nsec\nrounds: 24390"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 5691216.255887212,
            "unit": "iter/sec",
            "range": "stddev: 2.8507966502855517e-8",
            "extra": "mean: 175.7093659840393 nsec\nrounds: 197746"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1444778.972378914,
            "unit": "iter/sec",
            "range": "stddev: 7.151425368110384e-8",
            "extra": "mean: 692.1473935583662 nsec\nrounds: 70767"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1051385.725390346,
            "unit": "iter/sec",
            "range": "stddev: 1.541841089272553e-7",
            "extra": "mean: 951.1257151876699 nsec\nrounds: 168663"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 3624467.0151919164,
            "unit": "iter/sec",
            "range": "stddev: 4.840566207914947e-8",
            "extra": "mean: 275.90263501047474 nsec\nrounds: 190187"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 6242063.773522727,
            "unit": "iter/sec",
            "range": "stddev: 1.4855404971760244e-8",
            "extra": "mean: 160.20342570701533 nsec\nrounds: 60046"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 100418.65573661766,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011878405658165944",
            "extra": "mean: 9.958308968234377 usec\nrounds: 65955"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 56434.55669668667,
            "unit": "iter/sec",
            "range": "stddev: 0.000001622109592443792",
            "extra": "mean: 17.719639499865355 usec\nrounds: 43190"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 54768.5993222796,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016138745044890802",
            "extra": "mean: 18.258637474287294 usec\nrounds: 38960"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1436636.6124569003,
            "unit": "iter/sec",
            "range": "stddev: 3.1288511274267795e-7",
            "extra": "mean: 696.0702458291278 nsec\nrounds: 146628"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 996653.9982035739,
            "unit": "iter/sec",
            "range": "stddev: 1.7120565208854886e-7",
            "extra": "mean: 1.0033572351111393 usec\nrounds: 193874"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 357712.0028473221,
            "unit": "iter/sec",
            "range": "stddev: 5.955306429772223e-7",
            "extra": "mean: 2.7955449972049666 usec\nrounds: 39358"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 55231.1677358915,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017278303893233047",
            "extra": "mean: 18.105718944453145 usec\nrounds: 15271"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 56307.84454110561,
            "unit": "iter/sec",
            "range": "stddev: 0.000002425323510532365",
            "extra": "mean: 17.759514826925834 usec\nrounds: 26607"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1624.2724117091736,
            "unit": "iter/sec",
            "range": "stddev: 0.000014457579663693351",
            "extra": "mean: 615.6602752045328 usec\nrounds: 367"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 44155.04837167692,
            "unit": "iter/sec",
            "range": "stddev: 0.0000022631502565099564",
            "extra": "mean: 22.64746698004856 usec\nrounds: 23607"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 303073.50475248945,
            "unit": "iter/sec",
            "range": "stddev: 6.713030256114885e-7",
            "extra": "mean: 3.2995296003082433 usec\nrounds: 41486"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 6312.180054152912,
            "unit": "iter/sec",
            "range": "stddev: 0.000013999341318123322",
            "extra": "mean: 158.42387121737434 usec\nrounds: 4395"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 22814.034587813523,
            "unit": "iter/sec",
            "range": "stddev: 0.000003339999956040233",
            "extra": "mean: 43.832667832202105 usec\nrounds: 9438"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 197923.68025735382,
            "unit": "iter/sec",
            "range": "stddev: 8.691325670594582e-7",
            "extra": "mean: 5.052452534733247 usec\nrounds: 43358"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 212191.72413874543,
            "unit": "iter/sec",
            "range": "stddev: 8.41527554602148e-7",
            "extra": "mean: 4.7127191414219896 usec\nrounds: 74963"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 219836.55076952206,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010372432588323774",
            "extra": "mean: 4.5488341065194655 usec\nrounds: 86230"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 123818.03984550449,
            "unit": "iter/sec",
            "range": "stddev: 0.0000036245131028226397",
            "extra": "mean: 8.076367557165035 usec\nrounds: 38141"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 43693.81076578669,
            "unit": "iter/sec",
            "range": "stddev: 0.0000019057931256535736",
            "extra": "mean: 22.886536616371856 usec\nrounds: 17342"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 59427.94785091605,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016526028643003575",
            "extra": "mean: 16.82709964188315 usec\nrounds: 15084"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 54742.98715335076,
            "unit": "iter/sec",
            "range": "stddev: 0.000002476714711520931",
            "extra": "mean: 18.26717999875882 usec\nrounds: 100"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 213343.10525657228,
            "unit": "iter/sec",
            "range": "stddev: 9.879917846453292e-7",
            "extra": "mean: 4.6872852947245365 usec\nrounds: 69104"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 200528.55772607116,
            "unit": "iter/sec",
            "range": "stddev: 8.410591674815831e-7",
            "extra": "mean: 4.986820886459644 usec\nrounds: 71731"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 237687.61986112353,
            "unit": "iter/sec",
            "range": "stddev: 8.596748728655913e-7",
            "extra": "mean: 4.207202716676121 usec\nrounds: 43509"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 276818.4426660812,
            "unit": "iter/sec",
            "range": "stddev: 8.264377820488248e-7",
            "extra": "mean: 3.6124760704844867 usec\nrounds: 87674"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 44659.18655949496,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018912218740544404",
            "extra": "mean: 22.39180954780267 usec\nrounds: 7939"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 16097.750403200394,
            "unit": "iter/sec",
            "range": "stddev: 0.000004256193480415236",
            "extra": "mean: 62.1204811202185 usec\nrounds: 10249"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 89348.33282547016,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012799855177448396",
            "extra": "mean: 11.19215063534945 usec\nrounds: 21562"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 102796.91602147894,
            "unit": "iter/sec",
            "range": "stddev: 0.000001248980873997442",
            "extra": "mean: 9.727918294660265 usec\nrounds: 30867"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 25934.430842650738,
            "unit": "iter/sec",
            "range": "stddev: 0.000006424991618043496",
            "extra": "mean: 38.5587794876701 usec\nrounds: 6757"
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
          "id": "55253266591eeaffb5b3287c67728dad9777461a",
          "message": "Add repr, explain_failure and generators for is_protocol_p (#240)\n\n- Implement __repr__ and explain_failure for IsProtocolPredicate\n- Register generate_true/generate_false for IsProtocolPredicate\n- Document is_protocol_p and implements_protocol_p\n- Fix implies_p example in docs (implies_p is curried)\n\nCo-authored-by: Maurits Rijk <maurits.rijk@surf.nl>\nCo-authored-by: Claude Opus 5.5 (1M context) <noreply@anthropic.com>",
          "timestamp": "2026-10-16T11:05:48+02:00",
          "tree_id": "fb977f626d097612418713e18bb6f41a36cf7a1a",
          "url": "https://github.com/mrijk/py-predicate/commit/55253266591eeaffb5b3287c67728dad9777461a"
        },
        "date": 1792141595692,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 8227595.412700249,
            "unit": "iter/sec",
            "range": "stddev: 1.3721440937152868e-8",
            "extra": "mean: 121.54219426691591 nsec\nrounds: 80724"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 7079423.280098289,
            "unit": "iter/sec",
            "range": "stddev: 2.192858049389254e-8",
            "extra": "mean: 141.25444410298294 nsec\nrounds: 197317"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1756153.156187745,
            "unit": "iter/sec",
            "range": "stddev: 6.163559649603343e-8",
            "extra": "mean: 569.4264173238732 nsec\nrounds: 83767"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1285061.4307024935,
            "unit": "iter/sec",
            "range": "stddev: 6.955931313994085e-8",
            "extra": "mean: 778.1729154016697 nsec\nrounds: 62602"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4466308.867149006,
            "unit": "iter/sec",
            "range": "stddev: 3.319402110177369e-8",
            "extra": "mean: 223.89853226571262 nsec\nrounds: 195428"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7669849.462070519,
            "unit": "iter/sec",
            "range": "stddev: 1.5246920709392335e-8",
            "extra": "mean: 130.38065544118834 nsec\nrounds: 73584"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 117723.8239554272,
            "unit": "iter/sec",
            "range": "stddev: 9.615428880068169e-7",
            "extra": "mean: 8.494457335828828 usec\nrounds: 74184"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 71297.80296374,
            "unit": "iter/sec",
            "range": "stddev: 0.000004016012831118803",
            "extra": "mean: 14.025677628644056 usec\nrounds: 52089"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 69016.71047380746,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015485927863193278",
            "extra": "mean: 14.489244606630596 usec\nrounds: 47280"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1721901.130231019,
            "unit": "iter/sec",
            "range": "stddev: 2.4537553860709763e-7",
            "extra": "mean: 580.7534372579423 nsec\nrounds: 148810"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1281812.9643584844,
            "unit": "iter/sec",
            "range": "stddev: 6.946415156448228e-8",
            "extra": "mean: 780.1450194416431 nsec\nrounds: 61981"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 414179.1599193814,
            "unit": "iter/sec",
            "range": "stddev: 7.423719951789201e-7",
            "extra": "mean: 2.4144140912223753 usec\nrounds: 39670"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 64833.91629506057,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013502549027985612",
            "extra": "mean: 15.424025836245619 usec\nrounds: 16295"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 66238.89637757566,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015062693703659931",
            "extra": "mean: 15.096869885932117 usec\nrounds: 29551"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1880.932322917608,
            "unit": "iter/sec",
            "range": "stddev: 0.000013708667493612107",
            "extra": "mean: 531.6512390242995 usec\nrounds: 410"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 49845.49500218694,
            "unit": "iter/sec",
            "range": "stddev: 0.0000036362263735759954",
            "extra": "mean: 20.061993565439078 usec\nrounds: 25021"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 370230.70888707036,
            "unit": "iter/sec",
            "range": "stddev: 8.464302901905581e-7",
            "extra": "mean: 2.7010185162814926 usec\nrounds: 40559"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 7446.271207061802,
            "unit": "iter/sec",
            "range": "stddev: 0.000011733211952064518",
            "extra": "mean: 134.2954039938315 usec\nrounds: 5859"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 26091.325739672116,
            "unit": "iter/sec",
            "range": "stddev: 0.000003300085351460563",
            "extra": "mean: 38.3269140854537 usec\nrounds: 9847"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 229882.98873453125,
            "unit": "iter/sec",
            "range": "stddev: 9.619745941453193e-7",
            "extra": "mean: 4.350039146023108 usec\nrounds: 45062"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 242462.90721244592,
            "unit": "iter/sec",
            "range": "stddev: 7.282509286319446e-7",
            "extra": "mean: 4.124342199377327 usec\nrounds: 69629"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 256098.11059689798,
            "unit": "iter/sec",
            "range": "stddev: 7.093363803909029e-7",
            "extra": "mean: 3.904753524613128 usec\nrounds: 70717"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 150440.41810717198,
            "unit": "iter/sec",
            "range": "stddev: 9.616921443873962e-7",
            "extra": "mean: 6.647149832351648 usec\nrounds: 40265"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 51239.09723286951,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017798849600613372",
            "extra": "mean: 19.516346969487728 usec\nrounds: 17258"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 69507.99537870119,
            "unit": "iter/sec",
            "range": "stddev: 0.0000023583086242199176",
            "extra": "mean: 14.386834126803524 usec\nrounds: 11973"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 62743.65452205425,
            "unit": "iter/sec",
            "range": "stddev: 0.0000024182469034557486",
            "extra": "mean: 15.937866667433319 usec\nrounds: 120"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 248832.74615034132,
            "unit": "iter/sec",
            "range": "stddev: 0.0000020801832587034516",
            "extra": "mean: 4.018763669456164 usec\nrounds: 55507"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 223817.67084404558,
            "unit": "iter/sec",
            "range": "stddev: 0.0000031669401467628377",
            "extra": "mean: 4.46792246666168 usec\nrounds: 41092"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 279329.4932702634,
            "unit": "iter/sec",
            "range": "stddev: 6.820992450366018e-7",
            "extra": "mean: 3.5800014824516095 usec\nrounds: 39798"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 319150.62990536116,
            "unit": "iter/sec",
            "range": "stddev: 6.136773582769406e-7",
            "extra": "mean: 3.1333167047062807 usec\nrounds: 64467"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 52517.24466961007,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015829894680130386",
            "extra": "mean: 19.041364532565925 usec\nrounds: 7607"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 18915.636122673262,
            "unit": "iter/sec",
            "range": "stddev: 0.0000028845740227395736",
            "extra": "mean: 52.86631617962603 usec\nrounds: 9580"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 105090.24147849674,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011143205059087287",
            "extra": "mean: 9.515631384333789 usec\nrounds: 27039"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 122471.8849891801,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011093574591538477",
            "extra": "mean: 8.165139289628359 usec\nrounds: 22945"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 31307.02797777293,
            "unit": "iter/sec",
            "range": "stddev: 0.0000022572907391897916",
            "extra": "mean: 31.941709724409822 usec\nrounds: 6859"
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
          "id": "fecaf6a823fe4a8c33aea990dca17f7c6b985c73",
          "message": "Add generate_true and generate_false for same_signature_p (#241)",
          "timestamp": "2026-10-16T15:33:11+02:00",
          "tree_id": "2ab65dacf8a6de61742a2d5422852b92f1b1695e",
          "url": "https://github.com/mrijk/py-predicate/commit/fecaf6a823fe4a8c33aea990dca17f7c6b985c73"
        },
        "date": 1792157637829,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 9080577.838263646,
            "unit": "iter/sec",
            "range": "stddev: 1.090082185723183e-8",
            "extra": "mean: 110.12515038263429 nsec\nrounds: 88574"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 7848224.9532284625,
            "unit": "iter/sec",
            "range": "stddev: 1.3081552078908478e-8",
            "extra": "mean: 127.41734671973667 nsec\nrounds: 196657"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1856151.2816114838,
            "unit": "iter/sec",
            "range": "stddev: 4.2766539035253766e-8",
            "extra": "mean: 538.7491902771063 nsec\nrounds: 92192"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1272103.7854806106,
            "unit": "iter/sec",
            "range": "stddev: 1.0847083028023987e-7",
            "extra": "mean: 786.0993823095907 nsec\nrounds: 62248"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4456321.238130432,
            "unit": "iter/sec",
            "range": "stddev: 4.875396860619168e-8",
            "extra": "mean: 224.40033977881086 nsec\nrounds: 198177"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 8562350.658463316,
            "unit": "iter/sec",
            "range": "stddev: 1.0837082046585488e-8",
            "extra": "mean: 116.79035814908681 nsec\nrounds: 84825"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 138630.39345857885,
            "unit": "iter/sec",
            "range": "stddev: 7.356166855791838e-7",
            "extra": "mean: 7.213425390001423 usec\nrounds: 88145"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 77677.52436117832,
            "unit": "iter/sec",
            "range": "stddev: 0.0000031354766682474195",
            "extra": "mean: 12.873736749774432 usec\nrounds: 58150"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 75859.36170227532,
            "unit": "iter/sec",
            "range": "stddev: 0.0000019761746257584396",
            "extra": "mean: 13.182288613562196 usec\nrounds: 49717"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1849644.8361806588,
            "unit": "iter/sec",
            "range": "stddev: 2.0049290029347002e-7",
            "extra": "mean: 540.6443336791647 nsec\nrounds: 192197"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1301152.1328795773,
            "unit": "iter/sec",
            "range": "stddev: 4.8313870066904165e-8",
            "extra": "mean: 768.5496374562304 nsec\nrounds: 64268"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 456954.3832128659,
            "unit": "iter/sec",
            "range": "stddev: 3.568079954743959e-7",
            "extra": "mean: 2.18840224918942 usec\nrounds: 50685"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 60234.58025535743,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011009063061550715",
            "extra": "mean: 16.601759251257622 usec\nrounds: 18484"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 62472.26631963142,
            "unit": "iter/sec",
            "range": "stddev: 9.64907970230479e-7",
            "extra": "mean: 16.007102974040144 usec\nrounds: 25958"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1745.293318599251,
            "unit": "iter/sec",
            "range": "stddev: 0.000014007261369606591",
            "extra": "mean: 572.969591611447 usec\nrounds: 453"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 47023.089901186475,
            "unit": "iter/sec",
            "range": "stddev: 0.0000019176684734202687",
            "extra": "mean: 21.266148228484838 usec\nrounds: 26277"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 407014.8084862824,
            "unit": "iter/sec",
            "range": "stddev: 3.2887645092087384e-7",
            "extra": "mean: 2.4569130634805956 usec\nrounds: 52130"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 7394.614581921415,
            "unit": "iter/sec",
            "range": "stddev: 0.000019242783314357225",
            "extra": "mean: 135.23355259716053 usec\nrounds: 6122"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 24271.572685896597,
            "unit": "iter/sec",
            "range": "stddev: 0.000002498045659436211",
            "extra": "mean: 41.20046166522479 usec\nrounds: 11530"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 255117.2692843355,
            "unit": "iter/sec",
            "range": "stddev: 9.275325974146625e-7",
            "extra": "mean: 3.9197660072375244 usec\nrounds: 50852"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 278186.78292610333,
            "unit": "iter/sec",
            "range": "stddev: 6.693698686184668e-7",
            "extra": "mean: 3.5947070866613995 usec\nrounds: 70922"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 290144.47145289386,
            "unit": "iter/sec",
            "range": "stddev: 4.900867889427361e-7",
            "extra": "mean: 3.446558864253093 usec\nrounds: 87413"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 174517.38091100578,
            "unit": "iter/sec",
            "range": "stddev: 6.800249406407844e-7",
            "extra": "mean: 5.730088285647289 usec\nrounds: 44979"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 58286.52017512458,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011762061298327047",
            "extra": "mean: 17.156625528431846 usec\nrounds: 24365"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 76235.63887246935,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013502469004196677",
            "extra": "mean: 13.117224631288893 usec\nrounds: 18172"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 68903.85451487338,
            "unit": "iter/sec",
            "range": "stddev: 0.0000026555598734687163",
            "extra": "mean: 14.512976190383414 usec\nrounds: 84"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 285018.69143897976,
            "unit": "iter/sec",
            "range": "stddev: 4.659716829497341e-7",
            "extra": "mean: 3.508541825630029 usec\nrounds: 73400"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 260346.35664060735,
            "unit": "iter/sec",
            "range": "stddev: 5.463013458801368e-7",
            "extra": "mean: 3.8410370435121566 usec\nrounds: 74588"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 320525.35692268534,
            "unit": "iter/sec",
            "range": "stddev: 4.643513215004439e-7",
            "extra": "mean: 3.119877970344831 usec\nrounds: 50373"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 348361.7009298169,
            "unit": "iter/sec",
            "range": "stddev: 4.0913056889463917e-7",
            "extra": "mean: 2.870579622647629 usec\nrounds: 101554"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 59270.850822216555,
            "unit": "iter/sec",
            "range": "stddev: 0.0000028594477760028267",
            "extra": "mean: 16.871699766880504 usec\nrounds: 9869"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 21812.29873824844,
            "unit": "iter/sec",
            "range": "stddev: 0.000001932646256394947",
            "extra": "mean: 45.845695219939095 usec\nrounds: 11569"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 122320.09871559216,
            "unit": "iter/sec",
            "range": "stddev: 8.380876203917095e-7",
            "extra": "mean: 8.17527136178259 usec\nrounds: 40013"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 139590.17065219983,
            "unit": "iter/sec",
            "range": "stddev: 7.596257706937189e-7",
            "extra": "mean: 7.163828193115264 usec\nrounds: 36704"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 36722.278483297145,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013781962390283926",
            "extra": "mean: 27.231425753030074 usec\nrounds: 7502"
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
          "id": "c46aa42fa5f94ecf1134f93bb0a599940f4cac91",
          "message": "Implements protocol same signature (#242)",
          "timestamp": "2026-10-19T08:09:35+02:00",
          "tree_id": "79c552d86c6d202ae42c78ea0f2895b64ad8d881",
          "url": "https://github.com/mrijk/py-predicate/commit/c46aa42fa5f94ecf1134f93bb0a599940f4cac91"
        },
        "date": 1792390224949,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 8737317.872498037,
            "unit": "iter/sec",
            "range": "stddev: 1.3201810650281463e-8",
            "extra": "mean: 114.45159883076288 nsec\nrounds: 87245"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 7369139.51457025,
            "unit": "iter/sec",
            "range": "stddev: 2.0824377473097537e-8",
            "extra": "mean: 135.70105410852946 nsec\nrounds: 195695"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1457279.0177175712,
            "unit": "iter/sec",
            "range": "stddev: 2.944293045996417e-7",
            "extra": "mean: 686.2103878818117 nsec\nrounds: 198847"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1335578.2401074637,
            "unit": "iter/sec",
            "range": "stddev: 6.954476079532005e-8",
            "extra": "mean: 748.7393624498836 nsec\nrounds: 65579"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4528127.511047303,
            "unit": "iter/sec",
            "range": "stddev: 3.466014667711806e-8",
            "extra": "mean: 220.84183750574456 nsec\nrounds: 192308"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7859493.414190104,
            "unit": "iter/sec",
            "range": "stddev: 1.3092897183900351e-8",
            "extra": "mean: 127.23466352100084 nsec\nrounds: 77137"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 131563.13381138182,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012027266439393273",
            "extra": "mean: 7.600913500841888 usec\nrounds: 79284"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 73000.68066496636,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014366002400642468",
            "extra": "mean: 13.698502409716685 usec\nrounds: 52288"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 70041.7905916811,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014980494518945452",
            "extra": "mean: 14.277190682197814 usec\nrounds: 48080"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1713011.335087552,
            "unit": "iter/sec",
            "range": "stddev: 2.68195725411892e-7",
            "extra": "mean: 583.7672988596365 nsec\nrounds: 162814"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1286772.7114565026,
            "unit": "iter/sec",
            "range": "stddev: 7.182333560325508e-8",
            "extra": "mean: 777.1380221982611 nsec\nrounds: 61088"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 426303.96457770956,
            "unit": "iter/sec",
            "range": "stddev: 6.42772639420676e-7",
            "extra": "mean: 2.3457440772116334 usec\nrounds: 39719"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 62658.59255735483,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017546867935182668",
            "extra": "mean: 15.959503065515644 usec\nrounds: 18268"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 63931.24047762855,
            "unit": "iter/sec",
            "range": "stddev: 0.000002028658888290469",
            "extra": "mean: 15.64180504756403 usec\nrounds: 28053"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1749.620400246698,
            "unit": "iter/sec",
            "range": "stddev: 0.000017372499692332026",
            "extra": "mean: 571.5525492609707 usec\nrounds: 406"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 49182.61917867124,
            "unit": "iter/sec",
            "range": "stddev: 0.000002455988537526058",
            "extra": "mean: 20.332386048152244 usec\nrounds: 23624"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 363111.4356161588,
            "unit": "iter/sec",
            "range": "stddev: 6.671066991867726e-7",
            "extra": "mean: 2.7539755070041063 usec\nrounds: 42747"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 7115.808270175975,
            "unit": "iter/sec",
            "range": "stddev: 0.000013724407876881327",
            "extra": "mean: 140.53217316031896 usec\nrounds: 5082"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 22267.33756096358,
            "unit": "iter/sec",
            "range": "stddev: 0.000004761586984291889",
            "extra": "mean: 44.90882653852069 usec\nrounds: 10302"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 227446.29281128506,
            "unit": "iter/sec",
            "range": "stddev: 9.96604881004326e-7",
            "extra": "mean: 4.396642335382939 usec\nrounds: 49415"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 246554.0194809165,
            "unit": "iter/sec",
            "range": "stddev: 9.204594179447435e-7",
            "extra": "mean: 4.05590629633763 usec\nrounds: 93721"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 254492.16695675146,
            "unit": "iter/sec",
            "range": "stddev: 8.104878580129976e-7",
            "extra": "mean: 3.929394024020946 usec\nrounds: 95248"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 149973.11659195492,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011160475452620025",
            "extra": "mean: 6.667861698978945 usec\nrounds: 40542"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 50025.81428481312,
            "unit": "iter/sec",
            "range": "stddev: 0.00000225909436398311",
            "extra": "mean: 19.989679614342247 usec\nrounds: 21780"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 67217.4400758137,
            "unit": "iter/sec",
            "range": "stddev: 0.000001758746492677586",
            "extra": "mean: 14.87709140473235 usec\nrounds: 12472"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 60029.58073284293,
            "unit": "iter/sec",
            "range": "stddev: 0.000002772839409608292",
            "extra": "mean: 16.65845384545369 usec\nrounds: 130"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 252723.1258231315,
            "unit": "iter/sec",
            "range": "stddev: 7.966897478623234e-7",
            "extra": "mean: 3.956899459608025 usec\nrounds: 84374"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 227340.11927745165,
            "unit": "iter/sec",
            "range": "stddev: 0.000002833558595661401",
            "extra": "mean: 4.398695677552516 usec\nrounds: 83957"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 279918.76631622954,
            "unit": "iter/sec",
            "range": "stddev: 7.592865425584078e-7",
            "extra": "mean: 3.572465016047838 usec\nrounds: 49437"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 321977.0941532897,
            "unit": "iter/sec",
            "range": "stddev: 7.355705700234792e-7",
            "extra": "mean: 3.1058109976106287 usec\nrounds: 100422"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 51231.01245736218,
            "unit": "iter/sec",
            "range": "stddev: 0.00000197662224467229",
            "extra": "mean: 19.51942684779587 usec\nrounds: 9200"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 18589.52250628217,
            "unit": "iter/sec",
            "range": "stddev: 0.000003798899610007362",
            "extra": "mean: 53.79374320464974 usec\nrounds: 11184"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 104573.55865856119,
            "unit": "iter/sec",
            "range": "stddev: 0.00000231337983609469",
            "extra": "mean: 9.562646741946104 usec\nrounds: 42510"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 119623.46350953759,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012263009346804298",
            "extra": "mean: 8.359564007442987 usec\nrounds: 34207"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 30579.88116111681,
            "unit": "iter/sec",
            "range": "stddev: 0.0000027666016624606087",
            "extra": "mean: 32.70123892016718 usec\nrounds: 7965"
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
          "id": "fb505dd2dd00b1dadc2ac21d92f8f90d9e2d9e40",
          "message": "Is regex p (#244)",
          "timestamp": "2026-10-20T15:21:03+02:00",
          "tree_id": "327c998fb206113e10b3bdb9fae2d5a8c3bef965",
          "url": "https://github.com/mrijk/py-predicate/commit/fb505dd2dd00b1dadc2ac21d92f8f90d9e2d9e40"
        },
        "date": 1792502505865,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 15231464.761527305,
            "unit": "iter/sec",
            "range": "stddev: 7.61556982732579e-9",
            "extra": "mean: 65.65356751018915 nsec\nrounds: 100807"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 13713312.274212888,
            "unit": "iter/sec",
            "range": "stddev: 8.771089789803492e-9",
            "extra": "mean: 72.92184265944587 nsec\nrounds: 135337"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 3059023.104195361,
            "unit": "iter/sec",
            "range": "stddev: 4.6091302035509635e-8",
            "extra": "mean: 326.90174802162466 nsec\nrounds: 158379"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 2054027.4955287012,
            "unit": "iter/sec",
            "range": "stddev: 5.161600629407954e-8",
            "extra": "mean: 486.84840011968913 nsec\nrounds: 103789"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 6980792.772316044,
            "unit": "iter/sec",
            "range": "stddev: 1.5269563658021618e-8",
            "extra": "mean: 143.2502056164355 nsec\nrounds: 68866"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 14211267.491592411,
            "unit": "iter/sec",
            "range": "stddev: 8.111308308440764e-9",
            "extra": "mean: 70.36670026734872 nsec\nrounds: 121922"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 232200.446637184,
            "unit": "iter/sec",
            "range": "stddev: 5.246382904091206e-7",
            "extra": "mean: 4.306623929808851 usec\nrounds: 108743"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 130925.53837493216,
            "unit": "iter/sec",
            "range": "stddev: 7.614343819655934e-7",
            "extra": "mean: 7.637929256676377 usec\nrounds: 87245"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 124243.55636599104,
            "unit": "iter/sec",
            "range": "stddev: 9.55934710831187e-7",
            "extra": "mean: 8.048707146262341 usec\nrounds: 75816"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 3226653.05525941,
            "unit": "iter/sec",
            "range": "stddev: 1.2629169949018995e-7",
            "extra": "mean: 309.91866273630217 nsec\nrounds: 167955"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 2292939.0306468178,
            "unit": "iter/sec",
            "range": "stddev: 5.902360638256307e-8",
            "extra": "mean: 436.1214958768044 nsec\nrounds: 191132"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 725914.1190559607,
            "unit": "iter/sec",
            "range": "stddev: 3.850882876689303e-7",
            "extra": "mean: 1.377573426041752 usec\nrounds: 39121"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 108235.99102710345,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010461246150868377",
            "extra": "mean: 9.239070945907349 usec\nrounds: 21016"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 111005.17768464208,
            "unit": "iter/sec",
            "range": "stddev: 9.60774323394609e-7",
            "extra": "mean: 9.008588796109402 usec\nrounds: 37130"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 3117.207388770606,
            "unit": "iter/sec",
            "range": "stddev: 0.000014706711990912555",
            "extra": "mean: 320.799958194116 usec\nrounds: 598"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 83261.1961024315,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013711538132727543",
            "extra": "mean: 12.0103967611726 usec\nrounds: 36803"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 639425.0428309558,
            "unit": "iter/sec",
            "range": "stddev: 3.8317500009891856e-7",
            "extra": "mean: 1.5639049662062876 usec\nrounds: 63630"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 12383.067925768475,
            "unit": "iter/sec",
            "range": "stddev: 0.00000726519910520553",
            "extra": "mean: 80.75543201366567 usec\nrounds: 9296"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 42072.481084759886,
            "unit": "iter/sec",
            "range": "stddev: 0.000001938408832014299",
            "extra": "mean: 23.768505546069036 usec\nrounds: 14695"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 413203.05431139556,
            "unit": "iter/sec",
            "range": "stddev: 4.496259296416707e-7",
            "extra": "mean: 2.4201176384489793 usec\nrounds: 47935"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 437374.2244560058,
            "unit": "iter/sec",
            "range": "stddev: 4.6504722781402746e-7",
            "extra": "mean: 2.286371587726215 usec\nrounds: 134808"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 455070.5867067592,
            "unit": "iter/sec",
            "range": "stddev: 4.569267590535544e-7",
            "extra": "mean: 2.197461293283684 usec\nrounds: 96947"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 259901.2886774883,
            "unit": "iter/sec",
            "range": "stddev: 8.159561826244528e-7",
            "extra": "mean: 3.847614627416876 usec\nrounds: 50795"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 88476.08805452025,
            "unit": "iter/sec",
            "range": "stddev: 9.909102198349407e-7",
            "extra": "mean: 11.302488864378649 usec\nrounds: 27210"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 116867.45062561541,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012210212526009869",
            "extra": "mean: 8.556702440643612 usec\nrounds: 20732"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 91657.79033499406,
            "unit": "iter/sec",
            "range": "stddev: 0.0000023009010817277862",
            "extra": "mean: 10.910147368217862 usec\nrounds: 95"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 434159.06765683467,
            "unit": "iter/sec",
            "range": "stddev: 5.961253128591464e-7",
            "extra": "mean: 2.303303269460708 usec\nrounds: 115554"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 397516.4393731396,
            "unit": "iter/sec",
            "range": "stddev: 6.465273699159049e-7",
            "extra": "mean: 2.5156192321931194 usec\nrounds: 110939"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 497311.55476104474,
            "unit": "iter/sec",
            "range": "stddev: 4.186736425175405e-7",
            "extra": "mean: 2.0108119154410034 usec\nrounds: 72276"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 562218.434120257,
            "unit": "iter/sec",
            "range": "stddev: 3.755237255551295e-7",
            "extra": "mean: 1.778668110669069 usec\nrounds: 162973"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 92605.41971235278,
            "unit": "iter/sec",
            "range": "stddev: 9.868555627413774e-7",
            "extra": "mean: 10.798504051989177 usec\nrounds: 13080"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 32711.020751994725,
            "unit": "iter/sec",
            "range": "stddev: 0.000002490493610361538",
            "extra": "mean: 30.57073662059353 usec\nrounds: 17583"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 186134.68035200817,
            "unit": "iter/sec",
            "range": "stddev: 8.914366022380736e-7",
            "extra": "mean: 5.372453957042569 usec\nrounds: 54384"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 205350.86935276282,
            "unit": "iter/sec",
            "range": "stddev: 9.981721085429628e-7",
            "extra": "mean: 4.8697139834462835 usec\nrounds: 42536"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 54698.12049336349,
            "unit": "iter/sec",
            "range": "stddev: 0.0000024260702748857588",
            "extra": "mean: 18.282163829035586 usec\nrounds: 11042"
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
          "id": "44acb48760a49ebc88391c1c80e508e1cf27407d",
          "message": "Add random_functions and random_callable_objects (#245)\n\nrandom_callables now draws from lambdas, functions with random signatures\nand instances of a class implementing __call__.",
          "timestamp": "2026-10-21T22:13:25+02:00",
          "tree_id": "86555917cce390eb2af779f0bb5165c111a299c9",
          "url": "https://github.com/mrijk/py-predicate/commit/44acb48760a49ebc88391c1c80e508e1cf27407d"
        },
        "date": 1792613648343,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 12188300.389303142,
            "unit": "iter/sec",
            "range": "stddev: 9.663606637183277e-9",
            "extra": "mean: 82.04589385388246 nsec\nrounds: 116199"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 11074392.228391923,
            "unit": "iter/sec",
            "range": "stddev: 5.821138443337604e-9",
            "extra": "mean: 90.2984091024205 nsec\nrounds: 56421"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 2695272.6364346454,
            "unit": "iter/sec",
            "range": "stddev: 3.6347183991086567e-8",
            "extra": "mean: 371.01998012446626 nsec\nrounds: 123290"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1920343.9834179257,
            "unit": "iter/sec",
            "range": "stddev: 4.118522819191533e-8",
            "extra": "mean: 520.740038573792 nsec\nrounds: 94635"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 6168685.183473156,
            "unit": "iter/sec",
            "range": "stddev: 3.438830534744112e-8",
            "extra": "mean: 162.10909946890334 nsec\nrounds: 62985"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 11220417.817229902,
            "unit": "iter/sec",
            "range": "stddev: 1.9190944517582174e-8",
            "extra": "mean: 89.12324088898144 nsec\nrounds: 112537"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 177784.17040411086,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016127668073275665",
            "extra": "mean: 5.62479774058038 usec\nrounds: 102146"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 103805.33164011112,
            "unit": "iter/sec",
            "range": "stddev: 9.159356193154878e-7",
            "extra": "mean: 9.633416551925862 usec\nrounds: 69624"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 99529.79223501524,
            "unit": "iter/sec",
            "range": "stddev: 8.79234064200538e-7",
            "extra": "mean: 10.047242916359604 usec\nrounds: 53961"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 2257768.9768378553,
            "unit": "iter/sec",
            "range": "stddev: 1.8120787727770986e-7",
            "extra": "mean: 442.915112333841 nsec\nrounds: 180898"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1880967.8544685326,
            "unit": "iter/sec",
            "range": "stddev: 4.9770285159345304e-8",
            "extra": "mean: 531.6411961131307 nsec\nrounds: 90318"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 549983.4127244932,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010167562705305824",
            "extra": "mean: 1.818236653804206 usec\nrounds: 52000"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 83907.72436831154,
            "unit": "iter/sec",
            "range": "stddev: 0.000002896059615023828",
            "extra": "mean: 11.917853898772382 usec\nrounds: 19774"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 88505.19263514603,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015183624910650457",
            "extra": "mean: 11.298772085863954 usec\nrounds: 33087"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 2563.3982265539717,
            "unit": "iter/sec",
            "range": "stddev: 0.00000853367345965836",
            "extra": "mean: 390.10715917687133 usec\nrounds: 534"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 67609.49238657663,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013755191986111105",
            "extra": "mean: 14.790822482177704 usec\nrounds: 33315"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 522454.95573064056,
            "unit": "iter/sec",
            "range": "stddev: 3.2602612994646525e-7",
            "extra": "mean: 1.9140406058576365 usec\nrounds: 54943"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 9911.005252528077,
            "unit": "iter/sec",
            "range": "stddev: 0.0000103327980565023",
            "extra": "mean: 100.89793865712282 usec\nrounds: 7564"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 32579.197464529752,
            "unit": "iter/sec",
            "range": "stddev: 0.0000026996784887200547",
            "extra": "mean: 30.69443319126382 usec\nrounds: 12401"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 324438.20511507377,
            "unit": "iter/sec",
            "range": "stddev: 0.0000026052862631828347",
            "extra": "mean: 3.0822510550054174 usec\nrounds: 51188"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 344613.9350654547,
            "unit": "iter/sec",
            "range": "stddev: 6.20388295763734e-7",
            "extra": "mean: 2.901797920069784 usec\nrounds: 102702"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 352341.9255612293,
            "unit": "iter/sec",
            "range": "stddev: 5.658925048721178e-7",
            "extra": "mean: 2.8381521682585626 usec\nrounds: 107782"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 213291.60162320384,
            "unit": "iter/sec",
            "range": "stddev: 7.161936568581831e-7",
            "extra": "mean: 4.6884171359291384 usec\nrounds: 50806"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 71259.48112494875,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016403550931471161",
            "extra": "mean: 14.0332203408353 usec\nrounds: 28465"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 94948.31568359229,
            "unit": "iter/sec",
            "range": "stddev: 0.000001230938473683887",
            "extra": "mean: 10.532045700867622 usec\nrounds: 19168"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 83237.12097999161,
            "unit": "iter/sec",
            "range": "stddev: 0.0000020649860651963684",
            "extra": "mean: 12.013870593150118 usec\nrounds: 85"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 358542.41634010035,
            "unit": "iter/sec",
            "range": "stddev: 4.6770560246153166e-7",
            "extra": "mean: 2.789070286879074 usec\nrounds: 96405"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 326120.4873468493,
            "unit": "iter/sec",
            "range": "stddev: 5.408450168950742e-7",
            "extra": "mean: 3.0663513603070207 usec\nrounds: 102439"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 398806.6060737213,
            "unit": "iter/sec",
            "range": "stddev: 4.943728081221431e-7",
            "extra": "mean: 2.5074810315833767 usec\nrounds: 56067"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 441476.84579190635,
            "unit": "iter/sec",
            "range": "stddev: 5.745475659489632e-7",
            "extra": "mean: 2.2651244556353425 usec\nrounds: 138716"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 65267.35104919493,
            "unit": "iter/sec",
            "range": "stddev: 0.0000060449324080841275",
            "extra": "mean: 15.321596233410105 usec\nrounds: 11098"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 26398.80738121678,
            "unit": "iter/sec",
            "range": "stddev: 0.000004116700230480269",
            "extra": "mean: 37.8804991285901 usec\nrounds: 12622"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 151076.238294687,
            "unit": "iter/sec",
            "range": "stddev: 7.767551476982809e-7",
            "extra": "mean: 6.6191746054029705 usec\nrounds: 50302"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 168597.76856447334,
            "unit": "iter/sec",
            "range": "stddev: 7.034726005636029e-7",
            "extra": "mean: 5.931276602973489 usec\nrounds: 43651"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 44950.810331913504,
            "unit": "iter/sec",
            "range": "stddev: 0.000001937744822184676",
            "extra": "mean: 22.246539998190755 usec\nrounds: 9813"
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
          "id": "7ac1a83422a9611b35ade1a808c82c093fa3596a",
          "message": "Add filter_p ReactiveX operator (#246) (#247)\n\n* Add filter_p ReactiveX operator (#246)\n\n- Add predicate.rx.filter_p, with reactivex as optional \"rx\" extra\n- Enable ruff C901 (max-complexity 10), noqa existing offenders\n- Bump ruff pre-commit hook to v0.17.1\n- Remove .mutmut-cache from repo and ignore it",
          "timestamp": "2026-10-23T09:39:54+02:00",
          "tree_id": "5c691e9513036b63a81c50e1911b9cb889390da8",
          "url": "https://github.com/mrijk/py-predicate/commit/7ac1a83422a9611b35ade1a808c82c093fa3596a"
        },
        "date": 1792741244379,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 8887754.102755003,
            "unit": "iter/sec",
            "range": "stddev: 1.3075408562470383e-8",
            "extra": "mean: 112.51436397076091 nsec\nrounds: 87551"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 7634630.616885264,
            "unit": "iter/sec",
            "range": "stddev: 1.1237052786628005e-8",
            "extra": "mean: 130.98210642808738 nsec\nrounds: 74097"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1882306.7841864612,
            "unit": "iter/sec",
            "range": "stddev: 6.458632030750552e-8",
            "extra": "mean: 531.2630270480607 nsec\nrounds: 89840"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1285355.2112779825,
            "unit": "iter/sec",
            "range": "stddev: 6.70645189491376e-8",
            "extra": "mean: 777.9950563282316 nsec\nrounds: 64355"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4611632.8477178505,
            "unit": "iter/sec",
            "range": "stddev: 3.148628568629103e-8",
            "extra": "mean: 216.8429346006736 nsec\nrounds: 194175"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7946434.374609884,
            "unit": "iter/sec",
            "range": "stddev: 1.1810882758492125e-8",
            "extra": "mean: 125.8426047278712 nsec\nrounds: 78346"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 130793.23086919147,
            "unit": "iter/sec",
            "range": "stddev: 8.924963540038468e-7",
            "extra": "mean: 7.6456556150074535 usec\nrounds: 80561"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 72847.03796744374,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016425563973976797",
            "extra": "mean: 13.727394111026346 usec\nrounds: 53320"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 72528.7775044053,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012946954468789208",
            "extra": "mean: 13.78763070891773 usec\nrounds: 50513"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1699637.6608676976,
            "unit": "iter/sec",
            "range": "stddev: 2.837126822781473e-7",
            "extra": "mean: 588.3606977086404 nsec\nrounds: 157431"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1294344.0641248166,
            "unit": "iter/sec",
            "range": "stddev: 7.606170707842885e-8",
            "extra": "mean: 772.5921010625253 nsec\nrounds: 61388"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 429298.65982958383,
            "unit": "iter/sec",
            "range": "stddev: 5.051354133837542e-7",
            "extra": "mean: 2.3293806703169397 usec\nrounds: 46426"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 61076.59436689755,
            "unit": "iter/sec",
            "range": "stddev: 0.000004297992433270512",
            "extra": "mean: 16.372884087033878 usec\nrounds: 13467"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 63349.68174105072,
            "unit": "iter/sec",
            "range": "stddev: 0.0000032620177203694264",
            "extra": "mean: 15.785398955714058 usec\nrounds: 31026"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1752.9086611281216,
            "unit": "iter/sec",
            "range": "stddev: 0.00002052374550758423",
            "extra": "mean: 570.4803805102023 usec\nrounds: 431"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 48660.34697784787,
            "unit": "iter/sec",
            "range": "stddev: 0.000003073191705850296",
            "extra": "mean: 20.550613838722523 usec\nrounds: 28413"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 359678.5923793602,
            "unit": "iter/sec",
            "range": "stddev: 5.994769238660916e-7",
            "extra": "mean: 2.7802599909679357 usec\nrounds: 48594"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 7096.364141867468,
            "unit": "iter/sec",
            "range": "stddev: 0.000012934888313863735",
            "extra": "mean: 140.91723310817048 usec\nrounds: 5920"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 22740.52842035808,
            "unit": "iter/sec",
            "range": "stddev: 0.000004160296683512946",
            "extra": "mean: 43.97435193743197 usec\nrounds: 11252"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 233941.00548293022,
            "unit": "iter/sec",
            "range": "stddev: 8.270887963978284e-7",
            "extra": "mean: 4.274581952555411 usec\nrounds: 69406"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 246869.24049726943,
            "unit": "iter/sec",
            "range": "stddev: 7.473639390518427e-7",
            "extra": "mean: 4.05072741336951 usec\nrounds: 103424"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 254557.35111225536,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010984239704329233",
            "extra": "mean: 3.9283878294248016 usec\nrounds: 109806"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 155647.0037460564,
            "unit": "iter/sec",
            "range": "stddev: 9.450315405194291e-7",
            "extra": "mean: 6.424794412564056 usec\nrounds: 52367"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 49755.65342493633,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018861330959717174",
            "extra": "mean: 20.09821861768223 usec\nrounds: 26695"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 66768.03741170315,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015540612932330852",
            "extra": "mean: 14.977226211305702 usec\nrounds: 18801"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 60327.25131463466,
            "unit": "iter/sec",
            "range": "stddev: 0.0000030699955635256283",
            "extra": "mean: 16.576256637063324 usec\nrounds: 113"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 253379.3286770286,
            "unit": "iter/sec",
            "range": "stddev: 7.936209353670805e-7",
            "extra": "mean: 3.9466518647014635 usec\nrounds: 69315"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 229127.00867045607,
            "unit": "iter/sec",
            "range": "stddev: 7.539344510371976e-7",
            "extra": "mean: 4.364391635026575 usec\nrounds: 88488"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 278152.00706540013,
            "unit": "iter/sec",
            "range": "stddev: 6.937052051337905e-7",
            "extra": "mean: 3.595156513700353 usec\nrounds: 62461"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 327811.9183728837,
            "unit": "iter/sec",
            "range": "stddev: 6.443906697288448e-7",
            "extra": "mean: 3.0505297213218077 usec\nrounds: 110779"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 51375.29416228654,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017705142511386694",
            "extra": "mean: 19.464608744451294 usec\nrounds: 9789"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 18453.630040102093,
            "unit": "iter/sec",
            "range": "stddev: 0.000005304080115305657",
            "extra": "mean: 54.18988013886007 usec\nrounds: 12089"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 104903.16373133112,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012553486455376807",
            "extra": "mean: 9.532600966745992 usec\nrounds: 45307"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 122134.28379773058,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010694290555803304",
            "extra": "mean: 8.187709207482833 usec\nrounds: 40706"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 31100.928032222433,
            "unit": "iter/sec",
            "range": "stddev: 0.000002467343992497883",
            "extra": "mean: 32.15338137061183 usec\nrounds: 8653"
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
          "id": "df2110a6306bfd54d614e6e57f9f4af9a0e26431",
          "message": "Document and test beartype integration (#253)\n\nPredicates are callables, so they work directly as beartype validators via\nAnnotated[..., Is[predicate]]. Add a test and docs for this.\n\nSplit the integrations docs into one file per integration, included from\nintegrations.rst so the page layout stays the same. Also fix a malformed\nLaTeX link and an unknown lexer name that broke strict Sphinx builds.",
          "timestamp": "2026-10-23T14:28:14+02:00",
          "tree_id": "cd1e2dd60239d1888637056a0fa4f4740d11629a",
          "url": "https://github.com/mrijk/py-predicate/commit/df2110a6306bfd54d614e6e57f9f4af9a0e26431"
        },
        "date": 1792758541856,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 17409682.561610356,
            "unit": "iter/sec",
            "range": "stddev: 5.3112492503335476e-8",
            "extra": "mean: 57.439301173995794 nsec\nrounds: 177054"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 15582234.549852304,
            "unit": "iter/sec",
            "range": "stddev: 1.3728612614479036e-8",
            "extra": "mean: 64.17564803049885 nsec\nrounds: 80328"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 3679497.486120185,
            "unit": "iter/sec",
            "range": "stddev: 4.5412981050085755e-8",
            "extra": "mean: 271.77624221030294 nsec\nrounds: 173642"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 2344343.491593579,
            "unit": "iter/sec",
            "range": "stddev: 3.1827446751989946e-7",
            "extra": "mean: 426.55865217099443 nsec\nrounds: 117745"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 9332795.96115746,
            "unit": "iter/sec",
            "range": "stddev: 1.2442264973642055e-8",
            "extra": "mean: 107.14902631129411 nsec\nrounds: 93572"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 16121771.496884603,
            "unit": "iter/sec",
            "range": "stddev: 5.466599254372793e-9",
            "extra": "mean: 62.02792293596529 nsec\nrounds: 161839"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 246368.44866665124,
            "unit": "iter/sec",
            "range": "stddev: 3.925420069627654e-7",
            "extra": "mean: 4.0589613053619935 usec\nrounds: 108413"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 144451.45540480284,
            "unit": "iter/sec",
            "range": "stddev: 5.446688564299575e-7",
            "extra": "mean: 6.922740911108543 usec\nrounds: 93493"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 136910.99775366485,
            "unit": "iter/sec",
            "range": "stddev: 5.736242133094426e-7",
            "extra": "mean: 7.304015136893791 usec\nrounds: 75643"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 3033742.155566697,
            "unit": "iter/sec",
            "range": "stddev: 1.1118860070358749e-7",
            "extra": "mean: 329.6259038247771 nsec\nrounds: 153375"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 2506996.4236444607,
            "unit": "iter/sec",
            "range": "stddev: 3.8372100840720997e-8",
            "extra": "mean: 398.88369627040953 nsec\nrounds: 119718"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 779345.8700815969,
            "unit": "iter/sec",
            "range": "stddev: 3.1353155071954045e-7",
            "extra": "mean: 1.2831273487024457 usec\nrounds: 53169"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 127076.2786013121,
            "unit": "iter/sec",
            "range": "stddev: 5.704873610904139e-7",
            "extra": "mean: 7.869289304083184 usec\nrounds: 23439"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 129736.73496983672,
            "unit": "iter/sec",
            "range": "stddev: 5.82909514864898e-7",
            "extra": "mean: 7.707917115630327 usec\nrounds: 47524"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 3635.755895963766,
            "unit": "iter/sec",
            "range": "stddev: 0.000008878869525735072",
            "extra": "mean: 275.0459680503165 usec\nrounds: 626"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 93186.22591488187,
            "unit": "iter/sec",
            "range": "stddev: 9.409156137625768e-7",
            "extra": "mean: 10.73119970448658 usec\nrounds: 43319"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 676926.1418356339,
            "unit": "iter/sec",
            "range": "stddev: 2.332350510070321e-7",
            "extra": "mean: 1.477266038637953 usec\nrounds: 67509"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 13963.888296267607,
            "unit": "iter/sec",
            "range": "stddev: 0.000006166318744047811",
            "extra": "mean: 71.61329128272166 usec\nrounds: 10313"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 51410.5327135756,
            "unit": "iter/sec",
            "range": "stddev: 9.225043073764842e-7",
            "extra": "mean: 19.45126703065532 usec\nrounds: 16118"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 437616.82233422453,
            "unit": "iter/sec",
            "range": "stddev: 3.1750235064750156e-7",
            "extra": "mean: 2.2851041115514112 usec\nrounds: 69147"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 448080.60178589943,
            "unit": "iter/sec",
            "range": "stddev: 3.535941725370471e-7",
            "extra": "mean: 2.231741334068769 usec\nrounds: 162101"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 478685.52965963393,
            "unit": "iter/sec",
            "range": "stddev: 3.1087045925566806e-7",
            "extra": "mean: 2.0890541661266493 usec\nrounds: 181885"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 287824.66073515563,
            "unit": "iter/sec",
            "range": "stddev: 3.796227995194479e-7",
            "extra": "mean: 3.4743374575542667 usec\nrounds: 62799"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 92908.52854022456,
            "unit": "iter/sec",
            "range": "stddev: 8.203934326030255e-7",
            "extra": "mean: 10.76327454230482 usec\nrounds: 35011"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 124702.60745226413,
            "unit": "iter/sec",
            "range": "stddev: 5.799239213350065e-7",
            "extra": "mean: 8.019078513517032 usec\nrounds: 24378"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 107366.0515913472,
            "unit": "iter/sec",
            "range": "stddev: 0.0000029639729415708683",
            "extra": "mean: 9.313931034794537 usec\nrounds: 145"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 457144.206260242,
            "unit": "iter/sec",
            "range": "stddev: 3.478008668462978e-7",
            "extra": "mean: 2.187493544281566 usec\nrounds: 93406"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 402269.14674366143,
            "unit": "iter/sec",
            "range": "stddev: 0.0000034714229127633143",
            "extra": "mean: 2.48589783257037 usec\nrounds: 110084"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 529914.2937401297,
            "unit": "iter/sec",
            "range": "stddev: 3.820938563677579e-7",
            "extra": "mean: 1.8870976152426655 usec\nrounds: 75019"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 587289.0921121148,
            "unit": "iter/sec",
            "range": "stddev: 9.82543194947967e-7",
            "extra": "mean: 1.7027389294829571 usec\nrounds: 150151"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 98253.00093113049,
            "unit": "iter/sec",
            "range": "stddev: 7.558312984246224e-7",
            "extra": "mean: 10.177806179181648 usec\nrounds: 12073"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 35412.03602019426,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012086457678565518",
            "extra": "mean: 28.238986299170556 usec\nrounds: 18758"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 191305.71195506855,
            "unit": "iter/sec",
            "range": "stddev: 7.011282303302216e-7",
            "extra": "mean: 5.227235453559627 usec\nrounds: 71220"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 222731.65106815266,
            "unit": "iter/sec",
            "range": "stddev: 4.09614457514019e-7",
            "extra": "mean: 4.489707660336134 usec\nrounds: 58562"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 57309.76706610977,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011257386542690423",
            "extra": "mean: 17.449032707574062 usec\nrounds: 12627"
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
          "id": "df76fbaa91355a7cdacca1593fa85ee5d0d50486",
          "message": "Document and test pandera integration (#254)\n\n* Document and test pandera integration\n\nPredicates are callables, so they work directly as pandera element-wise\nchecks via pa.Check(predicate, element_wise=True). Add a test and docs.\n\nUse range predicates (ge_lt_p, ge_le_p) instead of combining ge_p and lt_p\nin the pandera and beartype examples.\n\nUpdate classifiers (add Testing and Quality Assurance, drop Internet and\nWeb Environment) and add keywords. Remove the unused and outdated\nrequirements/development.txt and its pre-commit hook.\n\n* Fix LaTeX example and show rendered output",
          "timestamp": "2026-10-23T15:50:59+02:00",
          "tree_id": "2e8b188494a4623d281b1954debfde8799538f2d",
          "url": "https://github.com/mrijk/py-predicate/commit/df76fbaa91355a7cdacca1593fa85ee5d0d50486"
        },
        "date": 1792763520560,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 7962234.321049263,
            "unit": "iter/sec",
            "range": "stddev: 1.86718758867926e-8",
            "extra": "mean: 125.59288758387356 nsec\nrounds: 197707"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 6943035.515774378,
            "unit": "iter/sec",
            "range": "stddev: 1.3357992332264078e-8",
            "extra": "mean: 144.02922147352245 nsec\nrounds: 66703"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1732317.6092177154,
            "unit": "iter/sec",
            "range": "stddev: 5.384586140859036e-8",
            "extra": "mean: 577.2613490037677 nsec\nrounds: 34937"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1215183.244314611,
            "unit": "iter/sec",
            "range": "stddev: 6.937111183347948e-8",
            "extra": "mean: 822.921155865691 nsec\nrounds: 59116"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4323911.684839516,
            "unit": "iter/sec",
            "range": "stddev: 3.318220750334496e-8",
            "extra": "mean: 231.2720686470532 nsec\nrounds: 195810"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7487747.57618822,
            "unit": "iter/sec",
            "range": "stddev: 1.1844086136186777e-8",
            "extra": "mean: 133.55151062785546 nsec\nrounds: 72407"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 121949.91328015001,
            "unit": "iter/sec",
            "range": "stddev: 9.231385074873379e-7",
            "extra": "mean: 8.20008783198349 usec\nrounds: 79561"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 67389.8059776238,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017478470428170416",
            "extra": "mean: 14.83903960685154 usec\nrounds: 52087"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 67318.39066327877,
            "unit": "iter/sec",
            "range": "stddev: 0.00000122933737345087",
            "extra": "mean: 14.85478173419089 usec\nrounds: 47937"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1726726.002664014,
            "unit": "iter/sec",
            "range": "stddev: 2.5902483885461413e-7",
            "extra": "mean: 579.1306776275957 nsec\nrounds: 146628"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1212590.6321078783,
            "unit": "iter/sec",
            "range": "stddev: 6.853344455829714e-8",
            "extra": "mean: 824.6806247065208 nsec\nrounds: 61181"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 433185.2980441088,
            "unit": "iter/sec",
            "range": "stddev: 6.302530438269016e-7",
            "extra": "mean: 2.3084809307128786 usec\nrounds: 47144"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 63941.601295957174,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012860913427395315",
            "extra": "mean: 15.639270517662602 usec\nrounds: 16827"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 66538.27593655417,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013479262119916233",
            "extra": "mean: 15.028943655731684 usec\nrounds: 28521"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1867.1475113330114,
            "unit": "iter/sec",
            "range": "stddev: 0.000014184828968301157",
            "extra": "mean: 535.5763237399871 usec\nrounds: 417"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 51066.70581153571,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017704815004930118",
            "extra": "mean: 19.58223042015969 usec\nrounds: 25996"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 371678.8854000682,
            "unit": "iter/sec",
            "range": "stddev: 4.90829892057411e-7",
            "extra": "mean: 2.6904945082463283 usec\nrounds: 44339"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 7341.960297054737,
            "unit": "iter/sec",
            "range": "stddev: 0.000011833513286128592",
            "extra": "mean: 136.2034061122824 usec\nrounds: 5432"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 26111.220443218754,
            "unit": "iter/sec",
            "range": "stddev: 0.000002661381845746962",
            "extra": "mean: 38.29771198073992 usec\nrounds: 8864"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 227078.0782491129,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010036988114202654",
            "extra": "mean: 4.4037716353357705 usec\nrounds: 25433"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 246035.23907982575,
            "unit": "iter/sec",
            "range": "stddev: 7.363469662097673e-7",
            "extra": "mean: 4.06445842367951 usec\nrounds: 99059"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 256839.17817506724,
            "unit": "iter/sec",
            "range": "stddev: 7.49898510353249e-7",
            "extra": "mean: 3.8934869948788653 usec\nrounds: 111186"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 152351.52856164527,
            "unit": "iter/sec",
            "range": "stddev: 9.33279164229481e-7",
            "extra": "mean: 6.563767422887226 usec\nrounds: 44596"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 51811.51333541606,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015047906960436102",
            "extra": "mean: 19.30072942525777 usec\nrounds: 21750"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 69137.48636114584,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012483323148912695",
            "extra": "mean: 14.463933426454217 usec\nrounds: 17184"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 62205.090184202745,
            "unit": "iter/sec",
            "range": "stddev: 0.000002171074098324857",
            "extra": "mean: 16.075854838225993 usec\nrounds: 124"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 258373.81999295574,
            "unit": "iter/sec",
            "range": "stddev: 7.070016546045404e-7",
            "extra": "mean: 3.8703611690505793 usec\nrounds: 81646"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 232312.02499188716,
            "unit": "iter/sec",
            "range": "stddev: 7.049956933644414e-7",
            "extra": "mean: 4.304555478929351 usec\nrounds: 89791"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 280571.1866251477,
            "unit": "iter/sec",
            "range": "stddev: 6.703710737747568e-7",
            "extra": "mean: 3.5641578596451984 usec\nrounds: 53915"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 331366.72715977917,
            "unit": "iter/sec",
            "range": "stddev: 6.386541342597041e-7",
            "extra": "mean: 3.0178044988741966 usec\nrounds: 102828"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 52402.74349750292,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014845867814787616",
            "extra": "mean: 19.08297034195646 usec\nrounds: 8834"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 18860.91542509755,
            "unit": "iter/sec",
            "range": "stddev: 0.000002684058376547903",
            "extra": "mean: 53.01969588757794 usec\nrounds: 11841"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 106427.14144099232,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010184664395689389",
            "extra": "mean: 9.39609940152759 usec\nrounds: 42947"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 122315.6792139026,
            "unit": "iter/sec",
            "range": "stddev: 9.431557681698839e-7",
            "extra": "mean: 8.175566750123874 usec\nrounds: 36764"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 31591.06343765744,
            "unit": "iter/sec",
            "range": "stddev: 0.000002300411815502174",
            "extra": "mean: 31.654521601446678 usec\nrounds: 7893"
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
          "id": "9b217b725eec32ab11db46a99a2900f8e719aac2",
          "message": "Document and test annotated-types integration (#255)",
          "timestamp": "2026-10-25T19:40:05+01:00",
          "tree_id": "b1fbc626669efa22f5311a313501028a54a5018f",
          "url": "https://github.com/mrijk/py-predicate/commit/9b217b725eec32ab11db46a99a2900f8e719aac2"
        },
        "date": 1792953658030,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 16934113.1397545,
            "unit": "iter/sec",
            "range": "stddev: 7.3927169826190125e-9",
            "extra": "mean: 59.05239865513839 nsec\nrounds: 95466"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 13737537.983124042,
            "unit": "iter/sec",
            "range": "stddev: 4.201150280094744e-8",
            "extra": "mean: 72.79324732193321 nsec\nrounds: 37340"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 3466003.895328195,
            "unit": "iter/sec",
            "range": "stddev: 2.853459401515416e-8",
            "extra": "mean: 288.5166982495011 nsec\nrounds: 167814"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 2416984.739418346,
            "unit": "iter/sec",
            "range": "stddev: 3.4504886763624277e-8",
            "extra": "mean: 413.7386486936003 nsec\nrounds: 113727"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 8869586.127659902,
            "unit": "iter/sec",
            "range": "stddev: 2.9711358146005083e-8",
            "extra": "mean: 112.7448322398594 nsec\nrounds: 90695"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 15415729.975814383,
            "unit": "iter/sec",
            "range": "stddev: 2.500044741633778e-8",
            "extra": "mean: 64.86880618490932 nsec\nrounds: 88992"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 241407.08191177525,
            "unit": "iter/sec",
            "range": "stddev: 8.472821410937547e-7",
            "extra": "mean: 4.142380546919748 usec\nrounds: 118737"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 138932.5896646801,
            "unit": "iter/sec",
            "range": "stddev: 8.658050383979305e-7",
            "extra": "mean: 7.197735264372052 usec\nrounds: 89969"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 133085.65363825153,
            "unit": "iter/sec",
            "range": "stddev: 7.873077223298529e-7",
            "extra": "mean: 7.513957911031964 usec\nrounds: 74295"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 2872538.109402623,
            "unit": "iter/sec",
            "range": "stddev: 4.538913497513871e-7",
            "extra": "mean: 348.1241891018676 nsec\nrounds: 171263"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 2469646.123195889,
            "unit": "iter/sec",
            "range": "stddev: 4.7506011526238305e-8",
            "extra": "mean: 404.91631193943385 nsec\nrounds: 111682"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 741284.3932886972,
            "unit": "iter/sec",
            "range": "stddev: 2.3709158858664293e-7",
            "extra": "mean: 1.3490099198817809 usec\nrounds: 50404"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 116195.27409423758,
            "unit": "iter/sec",
            "range": "stddev: 8.40353957423224e-7",
            "extra": "mean: 8.606201997414905 usec\nrounds: 15520"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 121199.54558451952,
            "unit": "iter/sec",
            "range": "stddev: 8.594114724904194e-7",
            "extra": "mean: 8.250856017464534 usec\nrounds: 33893"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 3449.222506053191,
            "unit": "iter/sec",
            "range": "stddev: 0.000007520890622178638",
            "extra": "mean: 289.9204090907607 usec\nrounds: 572"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 86372.04055014235,
            "unit": "iter/sec",
            "range": "stddev: 0.000005356381942043294",
            "extra": "mean: 11.577820711778378 usec\nrounds: 41107"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 639762.4527450904,
            "unit": "iter/sec",
            "range": "stddev: 8.999993972902203e-7",
            "extra": "mean: 1.5630801646911343 usec\nrounds: 52941"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 12923.419584557401,
            "unit": "iter/sec",
            "range": "stddev: 0.000007077824454518628",
            "extra": "mean: 77.37890064290193 usec\nrounds: 8555"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 48070.62295540231,
            "unit": "iter/sec",
            "range": "stddev: 0.000001921939340051",
            "extra": "mean: 20.802726041802153 usec\nrounds: 14254"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 411445.6125751824,
            "unit": "iter/sec",
            "range": "stddev: 0.000001918600179557302",
            "extra": "mean: 2.430454887442195 usec\nrounds: 53167"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 445073.0511551492,
            "unit": "iter/sec",
            "range": "stddev: 7.531757421523004e-7",
            "extra": "mean: 2.246822173134467 usec\nrounds: 95548"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 410123.23891459254,
            "unit": "iter/sec",
            "range": "stddev: 0.000004274564492059314",
            "extra": "mean: 2.4382914819617145 usec\nrounds: 111434"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 279274.8760279236,
            "unit": "iter/sec",
            "range": "stddev: 5.007482792008165e-7",
            "extra": "mean: 3.580701616353109 usec\nrounds: 51102"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 90803.51064509325,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016975733474197275",
            "extra": "mean: 11.012790066107835 usec\nrounds: 25408"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 120233.64763133955,
            "unit": "iter/sec",
            "range": "stddev: 7.054439417118166e-7",
            "extra": "mean: 8.317139334125503 usec\nrounds: 20964"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 108261.3873330171,
            "unit": "iter/sec",
            "range": "stddev: 0.000001964607133354833",
            "extra": "mean: 9.236903614803614 usec\nrounds: 166"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 460391.0796134072,
            "unit": "iter/sec",
            "range": "stddev: 4.12858936982318e-7",
            "extra": "mean: 2.172066411103589 usec\nrounds: 81914"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 417550.65693409427,
            "unit": "iter/sec",
            "range": "stddev: 6.163171408362662e-7",
            "extra": "mean: 2.394918995799446 usec\nrounds: 101575"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 508561.9092138338,
            "unit": "iter/sec",
            "range": "stddev: 3.522297077127531e-7",
            "extra": "mean: 1.9663289402579547 usec\nrounds: 59260"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 561998.2737772131,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011387879693256148",
            "extra": "mean: 1.779364896050231 usec\nrounds: 136036"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 75999.43005334467,
            "unit": "iter/sec",
            "range": "stddev: 0.000013563993357317368",
            "extra": "mean: 13.157993412557058 usec\nrounds: 10930"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 33673.10242300273,
            "unit": "iter/sec",
            "range": "stddev: 0.0000024781036533024865",
            "extra": "mean: 29.697293330384706 usec\nrounds: 13374"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 187339.7766854847,
            "unit": "iter/sec",
            "range": "stddev: 5.92738198905932e-7",
            "extra": "mean: 5.337894694295752 usec\nrounds: 53226"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 215073.69712493845,
            "unit": "iter/sec",
            "range": "stddev: 5.578532078805981e-7",
            "extra": "mean: 4.6495690238639 usec\nrounds: 45803"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 56623.258445274034,
            "unit": "iter/sec",
            "range": "stddev: 0.000001020973737252674",
            "extra": "mean: 17.660587317956857 usec\nrounds: 10645"
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
          "id": "fe652d37a543fb08def54bd572dc23f85a6b99c4",
          "message": "Bump version to 1.10.0\n\nCo-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com>",
          "timestamp": "2026-10-26T09:30:42+01:00",
          "tree_id": "3e0f2e983a3a86a42ff54d2abcd58cfa680625f2",
          "url": "https://github.com/mrijk/py-predicate/commit/fe652d37a543fb08def54bd572dc23f85a6b99c4"
        },
        "date": 1793003505006,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 8540413.870306663,
            "unit": "iter/sec",
            "range": "stddev: 1.6789108151099435e-8",
            "extra": "mean: 117.0903442369231 nsec\nrounds: 86423"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 7532123.587217551,
            "unit": "iter/sec",
            "range": "stddev: 1.9858397636293713e-8",
            "extra": "mean: 132.76468295037773 nsec\nrounds: 195351"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1841597.8131067287,
            "unit": "iter/sec",
            "range": "stddev: 6.472671821199001e-8",
            "extra": "mean: 543.0067264866183 nsec\nrounds: 30759"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1329950.6224608477,
            "unit": "iter/sec",
            "range": "stddev: 7.087634839451917e-8",
            "extra": "mean: 751.907614547125 nsec\nrounds: 64646"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4535407.330251693,
            "unit": "iter/sec",
            "range": "stddev: 3.36853783493659e-8",
            "extra": "mean: 220.48736247566654 nsec\nrounds: 198453"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7812123.536175683,
            "unit": "iter/sec",
            "range": "stddev: 1.2043203659071578e-8",
            "extra": "mean: 128.00616828053083 nsec\nrounds: 77858"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 130235.3074779121,
            "unit": "iter/sec",
            "range": "stddev: 9.570698190317178e-7",
            "extra": "mean: 7.678409329740323 usec\nrounds: 78223"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 71895.94252583742,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016460081574291537",
            "extra": "mean: 13.908990756197785 usec\nrounds: 53982"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 72368.42358571642,
            "unit": "iter/sec",
            "range": "stddev: 0.000001441007750743646",
            "extra": "mean: 13.818181334509173 usec\nrounds: 47735"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1713479.7942153232,
            "unit": "iter/sec",
            "range": "stddev: 2.433755051547986e-7",
            "extra": "mean: 583.6076990087552 nsec\nrounds: 173581"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1303067.8419021117,
            "unit": "iter/sec",
            "range": "stddev: 7.06954208752238e-8",
            "extra": "mean: 767.4197519449808 nsec\nrounds: 63252"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 432603.0754065069,
            "unit": "iter/sec",
            "range": "stddev: 5.240044085296812e-7",
            "extra": "mean: 2.3115878199902387 usec\nrounds: 48013"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 63214.58136790716,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018744210385281632",
            "extra": "mean: 15.81913505335149 usec\nrounds: 18178"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 64130.27929950555,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017522660607716447",
            "extra": "mean: 15.59325814456121 usec\nrounds: 28608"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1750.5259653969542,
            "unit": "iter/sec",
            "range": "stddev: 0.00001674453510679316",
            "extra": "mean: 571.2568792278595 usec\nrounds: 414"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 49005.308335715665,
            "unit": "iter/sec",
            "range": "stddev: 0.000002208340218593265",
            "extra": "mean: 20.4059526194469 usec\nrounds: 25960"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 354751.0302488717,
            "unit": "iter/sec",
            "range": "stddev: 0.0000048817327087344985",
            "extra": "mean: 2.8188783533580177 usec\nrounds: 44284"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 7031.55008727597,
            "unit": "iter/sec",
            "range": "stddev: 0.000012635197746255538",
            "extra": "mean: 142.21615256777628 usec\nrounds: 5355"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 22099.494285425015,
            "unit": "iter/sec",
            "range": "stddev: 0.0000039856002992607785",
            "extra": "mean: 45.24990423240213 usec\nrounds: 10160"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 224106.14841896726,
            "unit": "iter/sec",
            "range": "stddev: 8.013099939897682e-7",
            "extra": "mean: 4.462171194564891 usec\nrounds: 25509"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 238874.02231678535,
            "unit": "iter/sec",
            "range": "stddev: 8.135552749791266e-7",
            "extra": "mean: 4.186307034566694 usec\nrounds: 95429"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 253441.7555917053,
            "unit": "iter/sec",
            "range": "stddev: 8.541476571878256e-7",
            "extra": "mean: 3.9456797387838494 usec\nrounds: 90498"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 145231.46502153086,
            "unit": "iter/sec",
            "range": "stddev: 0.000002364931156099621",
            "extra": "mean: 6.88556023208709 usec\nrounds: 43266"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 50694.30962646939,
            "unit": "iter/sec",
            "range": "stddev: 0.0000024849531827693652",
            "extra": "mean: 19.726079857252117 usec\nrounds: 22415"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 67845.1885999209,
            "unit": "iter/sec",
            "range": "stddev: 0.000001757620980090226",
            "extra": "mean: 14.739438722721244 usec\nrounds: 16254"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 62271.16723551941,
            "unit": "iter/sec",
            "range": "stddev: 0.0000024505460399958345",
            "extra": "mean: 16.058796460613014 usec\nrounds: 113"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 259915.1775738223,
            "unit": "iter/sec",
            "range": "stddev: 8.608297990413399e-7",
            "extra": "mean: 3.847409025261618 usec\nrounds: 79599"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 232779.73422633074,
            "unit": "iter/sec",
            "range": "stddev: 9.309162183248894e-7",
            "extra": "mean: 4.295906614566817 usec\nrounds: 86566"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 278366.10390461056,
            "unit": "iter/sec",
            "range": "stddev: 7.381689651332461e-7",
            "extra": "mean: 3.5923914081962947 usec\nrounds: 48977"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 322069.4956052896,
            "unit": "iter/sec",
            "range": "stddev: 6.90627959387105e-7",
            "extra": "mean: 3.1049199431961862 usec\nrounds: 99217"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 51691.25334460139,
            "unit": "iter/sec",
            "range": "stddev: 0.000002200372614395861",
            "extra": "mean: 19.345632680513045 usec\nrounds: 8886"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 18639.298874712887,
            "unit": "iter/sec",
            "range": "stddev: 0.0000034764793437453642",
            "extra": "mean: 53.65008666482921 usec\nrounds: 11031"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 104868.9575868787,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013622183027764706",
            "extra": "mean: 9.535710309426408 usec\nrounds: 40526"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 122350.76204043475,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012210488932003435",
            "extra": "mean: 8.173222490183736 usec\nrounds: 33997"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 30672.44737665142,
            "unit": "iter/sec",
            "range": "stddev: 0.0000031537112788057507",
            "extra": "mean: 32.6025500254415 usec\nrounds: 7856"
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
          "id": "38fa0805c7d858587017971b9be33991ec798206",
          "message": "Bump version to 1.11.0\n\nCo-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com>",
          "timestamp": "2026-10-26T12:17:39+01:00",
          "tree_id": "3ccbcee3c72a10d5d8402afb29dc03ba7091f0d7",
          "url": "https://github.com/mrijk/py-predicate/commit/38fa0805c7d858587017971b9be33991ec798206"
        },
        "date": 1793013538507,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 9145128.13541352,
            "unit": "iter/sec",
            "range": "stddev: 1.1973495536947106e-8",
            "extra": "mean: 109.34783911092597 nsec\nrounds: 88098"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 7403992.537987083,
            "unit": "iter/sec",
            "range": "stddev: 1.9047391999794066e-8",
            "extra": "mean: 135.06226469967098 nsec\nrounds: 195313"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1799984.2820262394,
            "unit": "iter/sec",
            "range": "stddev: 5.637667066730221e-8",
            "extra": "mean: 555.5604068243872 nsec\nrounds: 86573"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1242460.9103752743,
            "unit": "iter/sec",
            "range": "stddev: 2.4449895077082047e-7",
            "extra": "mean: 804.854294931467 nsec\nrounds: 62306"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4566896.119641407,
            "unit": "iter/sec",
            "range": "stddev: 3.2411749203075185e-8",
            "extra": "mean: 218.9671001490877 nsec\nrounds: 196464"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7992446.758516762,
            "unit": "iter/sec",
            "range": "stddev: 1.1620985217967174e-8",
            "extra": "mean: 125.1181309321077 nsec\nrounds: 78285"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 131131.93389106155,
            "unit": "iter/sec",
            "range": "stddev: 0.000001028640833192315",
            "extra": "mean: 7.625907514112882 usec\nrounds: 79158"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 73384.505753168,
            "unit": "iter/sec",
            "range": "stddev: 0.000001295720651441618",
            "extra": "mean: 13.626854739112693 usec\nrounds: 52953"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 72658.75192903711,
            "unit": "iter/sec",
            "range": "stddev: 0.0000026934300314709115",
            "extra": "mean: 13.762966930352176 usec\nrounds: 49683"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1693727.3364134002,
            "unit": "iter/sec",
            "range": "stddev: 2.7055726443792115e-7",
            "extra": "mean: 590.413804218085 nsec\nrounds: 164718"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1232763.207107661,
            "unit": "iter/sec",
            "range": "stddev: 7.068099602989515e-8",
            "extra": "mean: 811.1857932118403 nsec\nrounds: 60274"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 428654.8972280198,
            "unit": "iter/sec",
            "range": "stddev: 6.21590529519025e-7",
            "extra": "mean: 2.3328789813593507 usec\nrounds: 52149"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 62124.545508621275,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018123199789596147",
            "extra": "mean: 16.0966972363802 usec\nrounds: 18526"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 63704.49328539414,
            "unit": "iter/sec",
            "range": "stddev: 0.000002114182921474378",
            "extra": "mean: 15.697479854678873 usec\nrounds: 29461"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1632.195759150302,
            "unit": "iter/sec",
            "range": "stddev: 0.00015430097937139752",
            "extra": "mean: 612.6716077981883 usec\nrounds: 436"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 49060.11199198461,
            "unit": "iter/sec",
            "range": "stddev: 0.0000021190352155072587",
            "extra": "mean: 20.3831577099412 usec\nrounds: 27912"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 355384.2036905861,
            "unit": "iter/sec",
            "range": "stddev: 6.227947635633355e-7",
            "extra": "mean: 2.8138560735542604 usec\nrounds: 43953"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 7071.495180027672,
            "unit": "iter/sec",
            "range": "stddev: 0.00001767463161626346",
            "extra": "mean: 141.4128093906283 usec\nrounds: 5367"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 22669.469239030517,
            "unit": "iter/sec",
            "range": "stddev: 0.0000040613032720058754",
            "extra": "mean: 44.11219289943843 usec\nrounds: 10985"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 229661.43069312282,
            "unit": "iter/sec",
            "range": "stddev: 9.109269915774283e-7",
            "extra": "mean: 4.354235698096889 usec\nrounds: 49364"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 241181.8975858727,
            "unit": "iter/sec",
            "range": "stddev: 7.905093153280703e-7",
            "extra": "mean: 4.1462481637700455 usec\nrounds: 93809"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 249946.6475370246,
            "unit": "iter/sec",
            "range": "stddev: 8.032975445979922e-7",
            "extra": "mean: 4.000853821621552 usec\nrounds: 97381"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 150338.9347318729,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012656096450118775",
            "extra": "mean: 6.651636861625261 usec\nrounds: 45999"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 49756.307298279586,
            "unit": "iter/sec",
            "range": "stddev: 0.0000036306629512513517",
            "extra": "mean: 20.09795449660664 usec\nrounds: 23251"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 66367.47880069606,
            "unit": "iter/sec",
            "range": "stddev: 0.000002445138408372827",
            "extra": "mean: 15.067620739414197 usec\nrounds: 15902"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 61384.04356868404,
            "unit": "iter/sec",
            "range": "stddev: 0.000002665748879459713",
            "extra": "mean: 16.29087857141696 usec\nrounds: 140"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 248301.5498786213,
            "unit": "iter/sec",
            "range": "stddev: 9.785570353255708e-7",
            "extra": "mean: 4.027361087713048 usec\nrounds: 86641"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 226403.47872465072,
            "unit": "iter/sec",
            "range": "stddev: 8.840723367104657e-7",
            "extra": "mean: 4.416893263447547 usec\nrounds: 84732"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 272670.3726078998,
            "unit": "iter/sec",
            "range": "stddev: 7.651206184584329e-7",
            "extra": "mean: 3.667431816796616 usec\nrounds: 49609"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 316930.31012110354,
            "unit": "iter/sec",
            "range": "stddev: 6.85445471659108e-7",
            "extra": "mean: 3.1552677925247536 usec\nrounds: 96164"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 50190.72335205995,
            "unit": "iter/sec",
            "range": "stddev: 0.0000028735096842378876",
            "extra": "mean: 19.924000556548215 usec\nrounds: 8985"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 18542.42030569581,
            "unit": "iter/sec",
            "range": "stddev: 0.0000037867047104161003",
            "extra": "mean: 53.93039223109524 usec\nrounds: 11353"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 103597.07015030994,
            "unit": "iter/sec",
            "range": "stddev: 0.000001322018861515526",
            "extra": "mean: 9.652782637087041 usec\nrounds: 39878"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 118498.39663239545,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011004520234813923",
            "extra": "mean: 8.438932748619292 usec\nrounds: 35345"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 30662.569176431018,
            "unit": "iter/sec",
            "range": "stddev: 0.000002725962757332797",
            "extra": "mean: 32.61305320653484 usec\nrounds: 7781"
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
          "id": "88119338db37ff07819ca711be6c0c324d9f9ef0",
          "message": "Remove unused test helpers\n\nCo-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com>",
          "timestamp": "2026-10-26T12:43:04+01:00",
          "tree_id": "64d9174450bf79f506f3e79f34846cc452c0066f",
          "url": "https://github.com/mrijk/py-predicate/commit/88119338db37ff07819ca711be6c0c324d9f9ef0"
        },
        "date": 1793015072597,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 10948660.475130191,
            "unit": "iter/sec",
            "range": "stddev: 9.733692999409495e-9",
            "extra": "mean: 91.33537406438838 nsec\nrounds: 101266"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 9391144.886380918,
            "unit": "iter/sec",
            "range": "stddev: 9.27291894406431e-9",
            "extra": "mean: 106.48328953482601 nsec\nrounds: 88207"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 2247593.0361959757,
            "unit": "iter/sec",
            "range": "stddev: 4.521635487767742e-8",
            "extra": "mean: 444.9204032472391 nsec\nrounds: 106907"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1641267.1418278893,
            "unit": "iter/sec",
            "range": "stddev: 5.4956887163545334e-8",
            "extra": "mean: 609.2853347970482 nsec\nrounds: 78809"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 5814624.729739389,
            "unit": "iter/sec",
            "range": "stddev: 1.4608728357914686e-8",
            "extra": "mean: 171.98014428780166 nsec\nrounds: 56415"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 10090122.254802553,
            "unit": "iter/sec",
            "range": "stddev: 8.784763199560831e-9",
            "extra": "mean: 99.10682692908246 nsec\nrounds: 95094"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 154562.4226724179,
            "unit": "iter/sec",
            "range": "stddev: 6.965521093574566e-7",
            "extra": "mean: 6.469877883057101 usec\nrounds: 98766"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 87819.2226887121,
            "unit": "iter/sec",
            "range": "stddev: 9.380404706084736e-7",
            "extra": "mean: 11.387028595603084 usec\nrounds: 66164"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 86139.84700112602,
            "unit": "iter/sec",
            "range": "stddev: 0.00000102024993775084",
            "extra": "mean: 11.609029210220537 usec\nrounds: 62170"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 2219195.541252207,
            "unit": "iter/sec",
            "range": "stddev: 1.7853138141130025e-7",
            "extra": "mean: 450.61373881264126 nsec\nrounds: 179244"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1587566.1855696707,
            "unit": "iter/sec",
            "range": "stddev: 5.597446184989695e-8",
            "extra": "mean: 629.8949984508313 nsec\nrounds: 77466"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 560589.3336583925,
            "unit": "iter/sec",
            "range": "stddev: 3.467026912731103e-7",
            "extra": "mean: 1.7838370085888435 usec\nrounds: 49702"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 84051.92020125873,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012016956038523632",
            "extra": "mean: 11.897408144936401 usec\nrounds: 21191"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 85618.57158830685,
            "unit": "iter/sec",
            "range": "stddev: 0.00000105003482967367",
            "extra": "mean: 11.6797089866023 usec\nrounds: 38524"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 2373.6534457986836,
            "unit": "iter/sec",
            "range": "stddev: 0.00003979250824886112",
            "extra": "mean: 421.2914912958246 usec\nrounds: 517"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 66745.01032767381,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013724260740336853",
            "extra": "mean: 14.982393366794943 usec\nrounds: 35458"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 475494.19239661156,
            "unit": "iter/sec",
            "range": "stddev: 3.784522695882464e-7",
            "extra": "mean: 2.1030751079413736 usec\nrounds: 52804"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 9543.336535334436,
            "unit": "iter/sec",
            "range": "stddev: 0.000008861787006041218",
            "extra": "mean: 104.78515520200672 usec\nrounds: 6411"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 33931.11986806987,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018683667006768959",
            "extra": "mean: 29.47147055234766 usec\nrounds: 11461"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 296342.11945932126,
            "unit": "iter/sec",
            "range": "stddev: 5.25742371209255e-7",
            "extra": "mean: 3.374478126243102 usec\nrounds: 58769"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 319238.3352811197,
            "unit": "iter/sec",
            "range": "stddev: 5.78915102770669e-7",
            "extra": "mean: 3.1324558785191163 usec\nrounds: 134753"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 332878.1655352572,
            "unit": "iter/sec",
            "range": "stddev: 5.291994129686362e-7",
            "extra": "mean: 3.0041021116300395 usec\nrounds: 89079"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 196946.3003381786,
            "unit": "iter/sec",
            "range": "stddev: 7.29947323986636e-7",
            "extra": "mean: 5.077526200202233 usec\nrounds: 47347"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 66590.72254771012,
            "unit": "iter/sec",
            "range": "stddev: 0.0000026232566515542254",
            "extra": "mean: 15.01710691430825 usec\nrounds: 26713"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 89189.49556190573,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014135321462933108",
            "extra": "mean: 11.212082697630104 usec\nrounds: 19009"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 80487.68923820656,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017379713154602984",
            "extra": "mean: 12.424260274642247 usec\nrounds: 146"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 332630.51227483427,
            "unit": "iter/sec",
            "range": "stddev: 5.106544233662424e-7",
            "extra": "mean: 3.0063387545570537 usec\nrounds: 94198"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 304628.1767415194,
            "unit": "iter/sec",
            "range": "stddev: 6.070243057653295e-7",
            "extra": "mean: 3.2826904283660916 usec\nrounds: 112562"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 359962.5466140431,
            "unit": "iter/sec",
            "range": "stddev: 4.798128677370152e-7",
            "extra": "mean: 2.778066800022431 usec\nrounds: 61482"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 426563.9215175129,
            "unit": "iter/sec",
            "range": "stddev: 4.945285147476232e-7",
            "extra": "mean: 2.3443145319052596 usec\nrounds: 147276"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 68697.84605289878,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011249752393043312",
            "extra": "mean: 14.556497145921854 usec\nrounds: 11037"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 25013.786026002454,
            "unit": "iter/sec",
            "range": "stddev: 0.000002538409077656867",
            "extra": "mean: 39.977954515181146 usec\nrounds: 15038"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 137189.6203296814,
            "unit": "iter/sec",
            "range": "stddev: 7.792268868768077e-7",
            "extra": "mean: 7.289181190216085 usec\nrounds: 26784"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 157532.17345213605,
            "unit": "iter/sec",
            "range": "stddev: 7.182302717097272e-7",
            "extra": "mean: 6.34790962433992 usec\nrounds: 37665"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 40827.180505248296,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015668347202666262",
            "extra": "mean: 24.493486633774552 usec\nrounds: 8080"
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
          "id": "1a69a117aef03749256a878e3bfdc5c1fc7bb34c",
          "message": "Add parentheses to repr of compound predicates where precedence requires (#256)\n\nCo-authored-by: Maurits Rijk <maurits.rijk@surf.nl>",
          "timestamp": "2026-10-26T12:44:53+01:00",
          "tree_id": "91713fb267258f23888230f25ebce34b070f9c92",
          "url": "https://github.com/mrijk/py-predicate/commit/1a69a117aef03749256a878e3bfdc5c1fc7bb34c"
        },
        "date": 1793015151977,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 7870160.579244144,
            "unit": "iter/sec",
            "range": "stddev: 6.807650946506457e-8",
            "extra": "mean: 127.06221047602065 nsec\nrounds: 200000"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 6835649.891991524,
            "unit": "iter/sec",
            "range": "stddev: 5.866230429185788e-8",
            "extra": "mean: 146.29186921518246 nsec\nrounds: 9940"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1706085.8494842374,
            "unit": "iter/sec",
            "range": "stddev: 5.997979292947715e-8",
            "extra": "mean: 586.1369756406499 nsec\nrounds: 83459"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1251269.5819660614,
            "unit": "iter/sec",
            "range": "stddev: 6.566049464292642e-8",
            "extra": "mean: 799.1882919656266 nsec\nrounds: 61966"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4276446.926490674,
            "unit": "iter/sec",
            "range": "stddev: 3.3291156966494795e-8",
            "extra": "mean: 233.83898296631435 nsec\nrounds: 192308"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7471223.919398103,
            "unit": "iter/sec",
            "range": "stddev: 1.200140512650975e-8",
            "extra": "mean: 133.84687847510827 nsec\nrounds: 73557"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 122295.02738732858,
            "unit": "iter/sec",
            "range": "stddev: 9.272830169172444e-7",
            "extra": "mean: 8.176947349076055 usec\nrounds: 73503"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 69164.70641137249,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013027255969860244",
            "extra": "mean: 14.45824108689593 usec\nrounds: 50824"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 67768.38557759582,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013888412579774754",
            "extra": "mean: 14.75614317025429 usec\nrounds: 46993"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1706670.8252560543,
            "unit": "iter/sec",
            "range": "stddev: 2.528900243666907e-7",
            "extra": "mean: 585.936072265118 nsec\nrounds: 164420"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1177297.293929299,
            "unit": "iter/sec",
            "range": "stddev: 1.1517231117735571e-7",
            "extra": "mean: 849.4031245603574 nsec\nrounds: 56680"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 417222.1131604461,
            "unit": "iter/sec",
            "range": "stddev: 5.813891201601982e-7",
            "extra": "mean: 2.3968048875095023 usec\nrounds: 43703"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 61309.53574028029,
            "unit": "iter/sec",
            "range": "stddev: 0.0000027604725191206853",
            "extra": "mean: 16.310676437613296 usec\nrounds: 16068"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 63069.96670454134,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016601547834190852",
            "extra": "mean: 15.85540713355086 usec\nrounds: 27588"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1690.8964651956146,
            "unit": "iter/sec",
            "range": "stddev: 0.000015435333421135882",
            "extra": "mean: 591.402265356509 usec\nrounds: 407"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 48186.130522922234,
            "unit": "iter/sec",
            "range": "stddev: 0.0000022403625768076607",
            "extra": "mean: 20.752859570749266 usec\nrounds: 27302"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 354229.54179182556,
            "unit": "iter/sec",
            "range": "stddev: 5.916518504351849e-7",
            "extra": "mean: 2.823028240224194 usec\nrounds: 48831"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 6838.92900490502,
            "unit": "iter/sec",
            "range": "stddev: 0.00001307202788137671",
            "extra": "mean: 146.2217255483687 usec\nrounds: 4376"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 20100.865262727202,
            "unit": "iter/sec",
            "range": "stddev: 0.000004163748054720053",
            "extra": "mean: 49.74910218687393 usec\nrounds: 9923"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 225556.24969837064,
            "unit": "iter/sec",
            "range": "stddev: 8.127049477446292e-7",
            "extra": "mean: 4.433483892985759 usec\nrounds: 67486"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 237359.15849746158,
            "unit": "iter/sec",
            "range": "stddev: 7.9566121275249e-7",
            "extra": "mean: 4.213024710444002 usec\nrounds: 100929"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 249860.46609276158,
            "unit": "iter/sec",
            "range": "stddev: 8.805250820524652e-7",
            "extra": "mean: 4.002233789273196 usec\nrounds: 106519"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 147362.77587390272,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010810343194377555",
            "extra": "mean: 6.785974233110897 usec\nrounds: 47464"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 48855.620323785115,
            "unit": "iter/sec",
            "range": "stddev: 0.0000020424731077486762",
            "extra": "mean: 20.46847411562094 usec\nrounds: 23547"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 65361.97210077588,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018225817379909032",
            "extra": "mean: 15.299415973223512 usec\nrounds: 18268"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 57362.78684846567,
            "unit": "iter/sec",
            "range": "stddev: 0.0000022845394082353516",
            "extra": "mean: 17.432904761787178 usec\nrounds: 147"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 241585.61542198737,
            "unit": "iter/sec",
            "range": "stddev: 7.805187648331915e-7",
            "extra": "mean: 4.139319297853308 usec\nrounds: 91150"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 224593.54369282722,
            "unit": "iter/sec",
            "range": "stddev: 8.519401070291917e-7",
            "extra": "mean: 4.452487740999728 usec\nrounds: 87405"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 262233.1987450254,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012086711154109623",
            "extra": "mean: 3.8133996945684983 usec\nrounds: 59588"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 313190.3661805647,
            "unit": "iter/sec",
            "range": "stddev: 7.278374520651161e-7",
            "extra": "mean: 3.1929462332933527 usec\nrounds: 105065"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 49972.81659872594,
            "unit": "iter/sec",
            "range": "stddev: 0.0000023800985764983127",
            "extra": "mean: 20.010879275223704 usec\nrounds: 8830"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 18273.993804960064,
            "unit": "iter/sec",
            "range": "stddev: 0.0000059850068522617105",
            "extra": "mean: 54.722575189260084 usec\nrounds: 11092"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 105886.29945510362,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013777313158205244",
            "extra": "mean: 9.444092438266816 usec\nrounds: 45598"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 121138.20441977822,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011475992535425021",
            "extra": "mean: 8.255034031499399 usec\nrounds: 37524"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 30639.793923153895,
            "unit": "iter/sec",
            "range": "stddev: 0.000002595418833062842",
            "extra": "mean: 32.63729522816142 usec\nrounds: 8634"
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
          "id": "c5185972e21e7052d00504660cfd902d2eb161b2",
          "message": "Resolve postponed annotations in spec and instrumentation (#260) (#271)\n\n* Resolve postponed annotations in spec and instrumentation (#260)\n\nWith `from __future__ import annotations`, signature() returned string\nannotations that ended up in isinstance(). Use eval_str=True, and resolve\nthe instrumented spec lazily on first call so forward references (e.g. the\nenclosing class) are defined by then. Unresolvable names raise a NameError\nnaming the function.\n\nCo-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com>\n\n* Test instrumenting functions with quoted annotations (#260)\n\nCo-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com>\n\n* Resolve nested string annotations with get_type_hints (#260)\n\nsignature(eval_str=True) evaluates an annotation only once, so x: \"str\"\nunder `from __future__ import annotations` stayed the string \"str\", and\nlist[\"int\"] kept a string inside the generic. get_type_hints resolves both.\n\nCo-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com>\n\n* Support callable instances in resolved_signature on Python < 3.14 (#260)\n\nget_type_hints only accepts callable instances from Python 3.14 on;\nread the hints from type(f).__call__ instead.\n\nCo-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com>\n\n---------\n\nCo-authored-by: Maurits Rijk <maurits.rijk@surf.nl>\nCo-authored-by: Claude Opus 5.5 (1M context) <noreply@anthropic.com>",
          "timestamp": "2026-10-26T13:32:52+01:00",
          "tree_id": "7ff8eaa2decfbd07326461f0ec42f6d00df91894",
          "url": "https://github.com/mrijk/py-predicate/commit/c5185972e21e7052d00504660cfd902d2eb161b2"
        },
        "date": 1793018033098,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 8599839.801798258,
            "unit": "iter/sec",
            "range": "stddev: 1.5932044552536205e-8",
            "extra": "mean: 116.28123581917146 nsec\nrounds: 84446"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 7399435.87023969,
            "unit": "iter/sec",
            "range": "stddev: 2.182493864886394e-8",
            "extra": "mean: 135.1454377788407 nsec\nrounds: 199243"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1866538.4568203858,
            "unit": "iter/sec",
            "range": "stddev: 5.866156306117852e-8",
            "extra": "mean: 535.7510831592946 nsec\nrounds: 88168"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1332138.1924869851,
            "unit": "iter/sec",
            "range": "stddev: 7.265949220569985e-8",
            "extra": "mean: 750.6728698567584 nsec\nrounds: 64268"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4558129.693498561,
            "unit": "iter/sec",
            "range": "stddev: 3.440184084473773e-8",
            "extra": "mean: 219.38822877864558 nsec\nrounds: 194591"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7868806.076942001,
            "unit": "iter/sec",
            "range": "stddev: 1.2170309092971577e-8",
            "extra": "mean: 127.08408241630262 nsec\nrounds: 78407"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 129625.31350164198,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010473496412835283",
            "extra": "mean: 7.714542576495545 usec\nrounds: 80232"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 71323.43614246683,
            "unit": "iter/sec",
            "range": "stddev: 0.000001414510161284892",
            "extra": "mean: 14.020636891393233 usec\nrounds: 53232"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 70536.57802285579,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015444611067524695",
            "extra": "mean: 14.177041586508105 usec\nrounds: 49391"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1758938.0268854657,
            "unit": "iter/sec",
            "range": "stddev: 2.862684654057935e-7",
            "extra": "mean: 568.5248625676086 nsec\nrounds: 154751"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1245486.607442783,
            "unit": "iter/sec",
            "range": "stddev: 7.130635069108798e-8",
            "extra": "mean: 802.8990388368665 nsec\nrounds: 25594"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 432220.5532563018,
            "unit": "iter/sec",
            "range": "stddev: 5.249715736352032e-7",
            "extra": "mean: 2.31363361243724 usec\nrounds: 48244"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 61831.91111115163,
            "unit": "iter/sec",
            "range": "stddev: 0.000008324602431721362",
            "extra": "mean: 16.17287872927554 usec\nrounds: 18636"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 64188.630630380794,
            "unit": "iter/sec",
            "range": "stddev: 0.000001651297363343637",
            "extra": "mean: 15.579082933834938 usec\nrounds: 28782"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1747.1482858057907,
            "unit": "iter/sec",
            "range": "stddev: 0.000017871876241602984",
            "extra": "mean: 572.3612632792623 usec\nrounds: 433"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 49015.80880723591,
            "unit": "iter/sec",
            "range": "stddev: 0.0000022209133883554862",
            "extra": "mean: 20.40158112931875 usec\nrounds: 25786"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 365277.13913682895,
            "unit": "iter/sec",
            "range": "stddev: 6.447770615596792e-7",
            "extra": "mean: 2.737647371973669 usec\nrounds: 45453"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 7117.790643798669,
            "unit": "iter/sec",
            "range": "stddev: 0.000013345366174239146",
            "extra": "mean: 140.49303358918596 usec\nrounds: 5210"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 22289.96146761565,
            "unit": "iter/sec",
            "range": "stddev: 0.000004277534868302373",
            "extra": "mean: 44.86324489402402 usec\nrounds: 10478"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 228399.44211191998,
            "unit": "iter/sec",
            "range": "stddev: 0.00000115902927305072",
            "extra": "mean: 4.37829440717277 usec\nrounds: 50386"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 258056.01968840812,
            "unit": "iter/sec",
            "range": "stddev: 8.95602664583957e-7",
            "extra": "mean: 3.875127583566771 usec\nrounds: 92073"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 243121.77525447975,
            "unit": "iter/sec",
            "range": "stddev: 0.000001389092234145473",
            "extra": "mean: 4.1131650957767265 usec\nrounds: 93897"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 154919.94022221412,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011449082098528864",
            "extra": "mean: 6.454946978198028 usec\nrounds: 43435"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 50061.155113452216,
            "unit": "iter/sec",
            "range": "stddev: 0.0000030464560564238195",
            "extra": "mean: 19.975567837652317 usec\nrounds: 22915"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 68057.85981843293,
            "unit": "iter/sec",
            "range": "stddev: 0.0000021973775327417583",
            "extra": "mean: 14.693380054380697 usec\nrounds: 17287"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 60320.38025944117,
            "unit": "iter/sec",
            "range": "stddev: 0.0000028240022866945005",
            "extra": "mean: 16.578144827651066 usec\nrounds: 145"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 262566.1035561842,
            "unit": "iter/sec",
            "range": "stddev: 7.963263224211794e-7",
            "extra": "mean: 3.8085647250579657 usec\nrounds: 82217"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 237765.44117322587,
            "unit": "iter/sec",
            "range": "stddev: 7.981692386286965e-7",
            "extra": "mean: 4.2058256871377795 usec\nrounds: 81348"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 285952.4685048318,
            "unit": "iter/sec",
            "range": "stddev: 7.190736236421343e-7",
            "extra": "mean: 3.4970846911332147 usec\nrounds: 49958"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 323350.5576952728,
            "unit": "iter/sec",
            "range": "stddev: 7.562977228361618e-7",
            "extra": "mean: 3.0926187575727178 usec\nrounds: 94074"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 51527.99599712391,
            "unit": "iter/sec",
            "range": "stddev: 0.0000019974804405973494",
            "extra": "mean: 19.40692589822077 usec\nrounds: 9352"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 18638.6727437973,
            "unit": "iter/sec",
            "range": "stddev: 0.000003602426259300256",
            "extra": "mean: 53.65188893789589 usec\nrounds: 11327"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 105548.46121817507,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013889768136178409",
            "extra": "mean: 9.47432097501582 usec\nrounds: 42913"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 121576.29309865258,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011335008001206488",
            "extra": "mean: 8.225287796762764 usec\nrounds: 19757"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 31004.187804073026,
            "unit": "iter/sec",
            "range": "stddev: 0.000002949511757697032",
            "extra": "mean: 32.2537073481612 usec\nrounds: 7866"
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
          "id": "1519f76249c695745e06a9db3ede5f0d69452a62",
          "message": "Add SpecViolationError for spec failures (#267) (#272)\n\ninstrument raised ValueError and exercise AssertionError. Both now raise\nSpecViolationError, which subclasses both for backwards compatibility.",
          "timestamp": "2026-10-26T14:03:08+01:00",
          "tree_id": "51315680265cc9ea75b56ac2bad269ea7915713d",
          "url": "https://github.com/mrijk/py-predicate/commit/1519f76249c695745e06a9db3ede5f0d69452a62"
        },
        "date": 1793019840694,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 16600147.56073658,
            "unit": "iter/sec",
            "range": "stddev: 7.887902592669528e-9",
            "extra": "mean: 60.24042836614569 nsec\nrounds: 152463"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 14474746.604180342,
            "unit": "iter/sec",
            "range": "stddev: 6.485596980014629e-9",
            "extra": "mean: 69.08583806995264 nsec\nrounds: 146199"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 3362569.2014699085,
            "unit": "iter/sec",
            "range": "stddev: 1.1040495206340326e-7",
            "extra": "mean: 297.39164908869725 nsec\nrounds: 167814"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 2343833.0596312787,
            "unit": "iter/sec",
            "range": "stddev: 4.443811933621232e-8",
            "extra": "mean: 426.6515466580694 nsec\nrounds: 114117"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 8833366.319403099,
            "unit": "iter/sec",
            "range": "stddev: 1.1351583717373059e-8",
            "extra": "mean: 113.20712442361086 nsec\nrounds: 90441"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 15690125.189554814,
            "unit": "iter/sec",
            "range": "stddev: 6.470045890517309e-9",
            "extra": "mean: 63.73435443751062 nsec\nrounds: 151976"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 245956.7788697594,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011283635375847727",
            "extra": "mean: 4.065754985877118 usec\nrounds: 117883"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 136497.71634855497,
            "unit": "iter/sec",
            "range": "stddev: 9.580742226373176e-7",
            "extra": "mean: 7.326129892506341 usec\nrounds: 80659"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 131817.56027496106,
            "unit": "iter/sec",
            "range": "stddev: 0.000001449478471168365",
            "extra": "mean: 7.586242666865316 usec\nrounds: 74184"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 2663113.2790334313,
            "unit": "iter/sec",
            "range": "stddev: 1.647730970078033e-7",
            "extra": "mean: 375.5003618783152 nsec\nrounds: 157506"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 2365807.199274212,
            "unit": "iter/sec",
            "range": "stddev: 4.244018531725055e-8",
            "extra": "mean: 422.6887128869937 nsec\nrounds: 107481"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 745290.5498405686,
            "unit": "iter/sec",
            "range": "stddev: 2.2829832105083235e-7",
            "extra": "mean: 1.341758593630254 usec\nrounds: 52335"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 120080.53231395228,
            "unit": "iter/sec",
            "range": "stddev: 6.635087390959091e-7",
            "extra": "mean: 8.327744562170041 usec\nrounds: 19907"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 121869.70166465624,
            "unit": "iter/sec",
            "range": "stddev: 6.460129378027765e-7",
            "extra": "mean: 8.205484926447577 usec\nrounds: 27200"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 3404.660184975523,
            "unit": "iter/sec",
            "range": "stddev: 0.00000830189383019536",
            "extra": "mean: 293.71506866174644 usec\nrounds: 568"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 87165.02026240379,
            "unit": "iter/sec",
            "range": "stddev: 0.000001486596578212236",
            "extra": "mean: 11.472492027072036 usec\nrounds: 35307"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 624914.9573295517,
            "unit": "iter/sec",
            "range": "stddev: 3.195153474160907e-7",
            "extra": "mean: 1.600217738863699 usec\nrounds: 52168"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 13230.60539263206,
            "unit": "iter/sec",
            "range": "stddev: 0.000006736714796325508",
            "extra": "mean: 75.582331293539 usec\nrounds: 8171"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 47977.51741075087,
            "unit": "iter/sec",
            "range": "stddev: 0.000001508426225510426",
            "extra": "mean: 20.843095974280622 usec\nrounds: 13389"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 428974.67175413715,
            "unit": "iter/sec",
            "range": "stddev: 3.9392949826931594e-7",
            "extra": "mean: 2.3311399619722555 usec\nrounds: 57287"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 448449.92957446317,
            "unit": "iter/sec",
            "range": "stddev: 3.7256491388085675e-7",
            "extra": "mean: 2.229903349408274 usec\nrounds: 94733"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 468920.7951596234,
            "unit": "iter/sec",
            "range": "stddev: 6.473952712416192e-7",
            "extra": "mean: 2.1325563087036783 usec\nrounds: 136018"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 272921.9966924561,
            "unit": "iter/sec",
            "range": "stddev: 4.766963611116005e-7",
            "extra": "mean: 3.664050578989632 usec\nrounds: 50001"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 92521.06090725784,
            "unit": "iter/sec",
            "range": "stddev: 9.222322370145019e-7",
            "extra": "mean: 10.808349906432545 usec\nrounds: 28319"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 124947.2195346886,
            "unit": "iter/sec",
            "range": "stddev: 7.109012714101281e-7",
            "extra": "mean: 8.00337937670053 usec\nrounds: 21849"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 101411.90897640894,
            "unit": "iter/sec",
            "range": "stddev: 0.0000025502916759793106",
            "extra": "mean: 9.8607748349617 usec\nrounds: 151"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 455124.1892013097,
            "unit": "iter/sec",
            "range": "stddev: 5.493073857542547e-7",
            "extra": "mean: 2.197202486105791 usec\nrounds: 73368"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 435663.26844469365,
            "unit": "iter/sec",
            "range": "stddev: 3.8929973090848344e-7",
            "extra": "mean: 2.2953507271108107 usec\nrounds: 94823"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 510784.5973343133,
            "unit": "iter/sec",
            "range": "stddev: 4.09216599658805e-7",
            "extra": "mean: 1.9577724254388404 usec\nrounds: 61448"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 590610.5180276403,
            "unit": "iter/sec",
            "range": "stddev: 3.504493188980546e-7",
            "extra": "mean: 1.6931632090460003 usec\nrounds: 146199"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 96767.94728867055,
            "unit": "iter/sec",
            "range": "stddev: 7.6296152053133e-7",
            "extra": "mean: 10.334000338116903 usec\nrounds: 11831"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 34216.744667741375,
            "unit": "iter/sec",
            "range": "stddev: 0.000001677900313875811",
            "extra": "mean: 29.225457000962837 usec\nrounds: 15698"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 188576.3792128797,
            "unit": "iter/sec",
            "range": "stddev: 6.436948981002553e-7",
            "extra": "mean: 5.302891084100847 usec\nrounds: 49653"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 217718.06640447307,
            "unit": "iter/sec",
            "range": "stddev: 5.075920921685982e-7",
            "extra": "mean: 4.593096092182889 usec\nrounds: 41814"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 56232.97581677739,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011633504417527947",
            "extra": "mean: 17.78315988928413 usec\nrounds: 10476"
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
          "id": "9345892926063507c4b0179cb887aec26dac7785",
          "message": "Support 'raises' in exercise and add InvalidSpecError (#264) (#273)\n\nexercise now catches exceptions: those matching spec['raises'] are yielded\nas the result, others raise SpecViolationError. Invalid specs raise the new\nInvalidSpecError (an AssertionError subclass) instead of a bare AssertionError.",
          "timestamp": "2026-10-26T15:14:11+01:00",
          "tree_id": "5cad9c579f2f5faa1293cb6e43e6b8ff90a15136",
          "url": "https://github.com/mrijk/py-predicate/commit/9345892926063507c4b0179cb887aec26dac7785"
        },
        "date": 1793024113165,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_eq",
            "value": 8224200.658161199,
            "unit": "iter/sec",
            "range": "stddev: 1.3050866737077128e-8",
            "extra": "mean: 121.59236399560127 nsec\nrounds: 80457"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_range",
            "value": 6907325.522156876,
            "unit": "iter/sec",
            "range": "stddev: 1.2750647525545866e-8",
            "extra": "mean: 144.77383421300533 nsec\nrounds: 67834"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_and_chain",
            "value": 1730483.6452650414,
            "unit": "iter/sec",
            "range": "stddev: 5.983292496381769e-8",
            "extra": "mean: 577.873129709261 nsec\nrounds: 83209"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_or_chain",
            "value": 1270448.4849489522,
            "unit": "iter/sec",
            "range": "stddev: 7.94812774355802e-8",
            "extra": "mean: 787.1236117379297 nsec\nrounds: 62020"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_not",
            "value": 4438198.14338851,
            "unit": "iter/sec",
            "range": "stddev: 3.2044019105706246e-8",
            "extra": "mean: 225.31666403621003 nsec\nrounds: 191278"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_in",
            "value": 7654611.06140668,
            "unit": "iter/sec",
            "range": "stddev: 1.1748783296020365e-8",
            "extra": "mean: 130.64021045325728 nsec\nrounds: 75076"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_all_list",
            "value": 119809.59959576056,
            "unit": "iter/sec",
            "range": "stddev: 9.434784166324847e-7",
            "extra": "mean: 8.346576596316284 usec\nrounds: 71322"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_any_list",
            "value": 67858.65753372066,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015439395938249753",
            "extra": "mean: 14.736513163454125 usec\nrounds: 52114"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_is_list_of",
            "value": 66549.5147454096,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012545294000466547",
            "extra": "mean: 15.026405584256755 usec\nrounds: 46703"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_regex",
            "value": 1927941.1190450718,
            "unit": "iter/sec",
            "range": "stddev: 2.488973637057735e-7",
            "extra": "mean: 518.6880398584527 nsec\nrounds: 156520"
          },
          {
            "name": "benchmarks/test_eval_bench.py::test_eval_nested_and_or",
            "value": 1211767.4800376084,
            "unit": "iter/sec",
            "range": "stddev: 7.81882805663992e-8",
            "extra": "mean: 825.2408291803343 nsec\nrounds: 59613"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_eq",
            "value": 435323.9753700969,
            "unit": "iter/sec",
            "range": "stddev: 4.4358213478955654e-7",
            "extra": "mean: 2.2971397317361983 usec\nrounds: 44657"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_range",
            "value": 64881.300847921564,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014368154034670061",
            "extra": "mean: 15.412761256805695 usec\nrounds: 17345"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_ge",
            "value": 66536.71623854131,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014507444922143705",
            "extra": "mean: 15.029295951650093 usec\nrounds: 30630"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_and",
            "value": 1869.0537284058755,
            "unit": "iter/sec",
            "range": "stddev: 0.000012371616066462002",
            "extra": "mean: 535.0300982802162 usec\nrounds: 407"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_or",
            "value": 50628.41909120016,
            "unit": "iter/sec",
            "range": "stddev: 0.0000018035753054600592",
            "extra": "mean: 19.751752433719822 usec\nrounds: 26195"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_in",
            "value": 373391.69692877674,
            "unit": "iter/sec",
            "range": "stddev: 5.036146296935512e-7",
            "extra": "mean: 2.6781527501152413 usec\nrounds: 42599"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_list_of",
            "value": 7389.2158245431365,
            "unit": "iter/sec",
            "range": "stddev: 0.000012221482979054566",
            "extra": "mean: 135.33235782321034 usec\nrounds: 5145"
          },
          {
            "name": "benchmarks/test_generator_bench.py::test_generate_true_regex",
            "value": 26415.196102717076,
            "unit": "iter/sec",
            "range": "stddev: 0.0000026022122080830965",
            "extra": "mean: 37.856997014576 usec\nrounds: 10719"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_idempotent_and",
            "value": 224060.75877995678,
            "unit": "iter/sec",
            "range": "stddev: 7.780804572853569e-7",
            "extra": "mean: 4.463075129465528 usec\nrounds: 48077"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_true",
            "value": 239777.90486328822,
            "unit": "iter/sec",
            "range": "stddev: 9.769853853831009e-7",
            "extra": "mean: 4.170526056477806 usec\nrounds: 75701"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_always_false",
            "value": 254683.93350770965,
            "unit": "iter/sec",
            "range": "stddev: 7.026961170425774e-7",
            "extra": "mean: 3.9264353515638177 usec\nrounds: 78254"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_range_from_and",
            "value": 149739.6860588756,
            "unit": "iter/sec",
            "range": "stddev: 9.525842577353906e-7",
            "extra": "mean: 6.678256288094617 usec\nrounds: 36100"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_and_chain",
            "value": 51394.64848065546,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015240680596132146",
            "extra": "mean: 19.45727871602025 usec\nrounds: 20250"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_intersection",
            "value": 68558.4159122904,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013220780231590002",
            "extra": "mean: 14.586101307815238 usec\nrounds: 16899"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_in_not_in",
            "value": 65187.08446130912,
            "unit": "iter/sec",
            "range": "stddev: 0.000002514540170068072",
            "extra": "mean: 15.340462121657488 usec\nrounds: 132"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_always_true",
            "value": 252985.1493525054,
            "unit": "iter/sec",
            "range": "stddev: 7.692393179689988e-7",
            "extra": "mean: 3.9528011923206456 usec\nrounds: 61562"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_or_idempotent",
            "value": 225978.1936153308,
            "unit": "iter/sec",
            "range": "stddev: 7.239826986423673e-7",
            "extra": "mean: 4.425205742206438 usec\nrounds: 66525"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_always_false",
            "value": 278037.0237812823,
            "unit": "iter/sec",
            "range": "stddev: 6.310892411945755e-7",
            "extra": "mean: 3.5966433045501502 usec\nrounds: 49653"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_not_not",
            "value": 324999.2479589737,
            "unit": "iter/sec",
            "range": "stddev: 6.65006388230828e-7",
            "extra": "mean: 3.0769301968545943 usec\nrounds: 89953"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_all_and",
            "value": 52446.21679536558,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016430541865271868",
            "extra": "mean: 19.06715223906036 usec\nrounds: 8999"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_deeply_nested",
            "value": 18801.74810762698,
            "unit": "iter/sec",
            "range": "stddev: 0.000002457923995339522",
            "extra": "mean: 53.18654384026915 usec\nrounds: 9010"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_is_list_of_and",
            "value": 103664.01858004073,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010500253317500767",
            "extra": "mean: 9.646548664596512 usec\nrounds: 34409"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_complement_and",
            "value": 119755.97196227727,
            "unit": "iter/sec",
            "range": "stddev: 0.000001010939889748307",
            "extra": "mean: 8.350314256686897 usec\nrounds: 30526"
          },
          {
            "name": "benchmarks/test_optimizer_bench.py::test_optimize_absorption",
            "value": 31214.522311744844,
            "unit": "iter/sec",
            "range": "stddev: 0.0000020403117037941747",
            "extra": "mean: 32.03637044362962 usec\nrounds: 6063"
          }
        ]
      }
    ]
  }
}