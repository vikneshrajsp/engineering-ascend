# Jekyll plugin to replace default Just the Docs footer with custom sponsorship footer
# This makes footer maintenance more manageable

Jekyll::Hooks.register :site, :post_write do |site|
  # Define the default footer text pattern
  default_footer_pattern = /This site uses <a href="https:\/\/github\.com\/just-the-docs\/just-the-docs"[^>]*>Just the Docs<\/a>, a documentation theme for Jekyll\./
  
  # Define the replacement text (our custom footer)
  replacement_footer = <<~HTML
    <!-- Custom Footer with Sponsorship -->
    <footer class="custom-footer">
      <div class="footer-content">
        <div class="sponsorship-section">
          <h3 class="sponsorship-title">Support Engineering Ascend</h3>
          <p class="sponsorship-description">
            If you find this documentation helpful for your system design interviews and learning, 
            consider supporting the project to keep it free and updated.
          </p>
          <div class="sponsorship-buttons">
            <a href="https://ko-fi.com/engineeringascend" target="_blank" class="ko-fi-btn">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M23.881 8.948c-.773-4.085-4.201-6.788-8.285-6.788-4.085 0-7.512 2.703-8.285 6.788C7.548 11.832 0 16.956 0 23.469c0 .767.629 1.346 1.396 1.346H22.602c.767 0 1.396-.58 1.396-1.346 0-6.513-7.548-11.637-16.119-14.521zM12 4.935c2.953 0 5.348 2.395 5.348 5.348S14.953 15.63 12 15.63s-5.348-2.395-5.348-5.348S9.047 4.935 12 4.935z"/>
              </svg>
              Buy Me a Coffee
            </a>
          </div>
        </div>
        <div class="footer-info">
          <p>&copy; 2024 Engineering Ascend. Empowering engineers to master system design.</p>
        </div>
      </div>
    </footer>
  HTML
  
  # Find all HTML files in the site destination
  site_dir = site.dest
  html_files = Dir.glob(File.join(site_dir, "**", "*.html"))
  
  replaced_count = 0
  
  html_files.each do |html_file|
    begin
      # Read the file
      content = File.read(html_file, encoding: 'utf-8')
      
      # Check if the default footer text exists
      if content.match?(default_footer_pattern)
        # Replace the default footer text
        new_content = content.gsub(default_footer_pattern, replacement_footer)
        
        # Write the updated content back
        File.write(html_file, new_content, encoding: 'utf-8')
        
        replaced_count += 1
        Jekyll.logger.info "✅ Updated footer in: #{html_file}"
      end
      
    rescue => e
      Jekyll.logger.error "❌ Error processing #{html_file}: #{e.message}"
    end
  end
  
  Jekyll.logger.info "🎉 Footer replacement complete! Updated #{replaced_count} files."
end
