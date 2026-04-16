window.BENCHMARK_DATA = {
  "lastUpdate": 1776354284201,
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
      }
    ]
  }
}