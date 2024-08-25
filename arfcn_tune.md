# Manual for Fine-Tuning ARFCN in YateBTS

Fine-tuning the ARFCN (Absolute Radio Frequency Channel Number) for YateBTS involves scanning and selecting the optimal frequency to ensure minimal interference and optimal signal quality. Below is a step-by-step guide to using the commands you've mentioned:

## Step-by-Step Guide

### 1. Check Current Noise Levels

- **Command:** `mbts noise`
- **Description:** This command checks the noise level across all ARFCNs. High noise levels can indicate interference from other signals, so it’s important to identify quieter frequencies.

  **Usage:**
  ```bash
  mbts noise
  ```
  **Output:**
  The command will output the noise level for each ARFCN. Lower values indicate less interference.

### 2. Start Scanning for Available ARFCNs

- **Command:** `mbts scan start`
- **Description:** This command starts the scanning process to detect available ARFCNs and measure their signal strength.

  **Usage:**
  ```bash
  mbts scan start
  ```
  **Output:**
  The scan will start in the background, and you may see a confirmation message indicating that the scan has started.

### 3. Monitor the Scan Progress

- **Command:** `mbts scan report`
- **Description:** Use this command to monitor the progress of the ongoing scan and see which ARFCNs have been scanned so far.

  **Usage:**
  ```bash
  mbts scan report
  ```
  **Output:**
  A report on the current scan progress, showing which frequencies have been checked and the signal strength measured.

### 4. List Scanned ARFCNs and Their Signal Strengths

- **Command:** `mbts scan list`
- **Description:** After scanning, this command lists all ARFCNs that have been scanned, along with their signal strength. This information helps identify the best ARFCNs to use.

  **Usage:**
  ```bash
  mbts scan list
  ```
  **Output:**
  A list of ARFCNs with corresponding signal strengths. Lower signal strength values typically indicate less interference.

### 5. Stop the Scanning Process

- **Command:** `mbts scan stop`
- **Description:** Once you have identified the optimal ARFCNs, use this command to stop the scanning process.

  **Usage:**
  ```bash
  mbts scan stop
  ```
  **Output:**
  The scanning process stops, and you may receive a confirmation message.

## Selecting the Optimal ARFCN

1. **Review the `mbts noise` and `mbts scan list` outputs** to identify ARFCNs with the least noise and interference.
2. **Choose an ARFCN** that shows the lowest noise level and interference for optimal signal quality.

## Applying the Selected ARFCN

To apply the selected ARFCN to YateBTS, you will need to edit the YateBTS configuration file (`ybts.conf`).

1. **Open the configuration file:**
   ```bash
   nano /usr/local/etc/yate/ybts.conf
   ```
2. **Find the `Radio.C0` parameter** and set it to the chosen ARFCN value.
3. **Save and exit** the file.
4. **Restart YateBTS** to apply the changes.

## Conclusion

By following these steps, you can effectively fine-tune the ARFCN for YateBTS, ensuring minimal interference and optimal performance. Make sure to periodically check noise levels and adjust the ARFCN as needed based on changes in the RF environment.
