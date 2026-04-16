window.BENCHMARK_DATA = {
  "lastUpdate": 1776350035148,
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
      }
    ]
  }
}